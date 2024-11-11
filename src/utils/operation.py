from datetime import datetime, timedelta
from io import BytesIO
from typing import Union

from sqlalchemy import insert, select, func, text, update
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from PIL import Image
import re

from models import Ban, Repository, User
from utils.protect import decrypt, encrypt_create, encrypt_delete
from config import setting
from database import get_async_session


# возваращет даные для отправки сообщения
def email_data() -> str:
    return setting.SMTP_USER, setting.SMTP_PASS

# удаление символов для создания учетной записи Postgresql
def delete_special_symbol(object: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]', '', object)

# Получение настоящего времени
def get_time() -> datetime:
    return datetime.now()

# проверка на наличие SQL инъекции
def contains_sql_injection(object: str) -> bool:
    sql_pattern = re.compile(r'\b(SELECT|INSERT|UPDATE|DELETE|DROP\
                            |CREATE|ALTER|UNION|AND|OR)\b', re.IGNORECASE)
    sql_injection_chars = ["'", '"', ';', '--', '#']
    if re.search(sql_pattern, object.upper()):
            return True
    for item in sql_injection_chars:
        if item in object:
            return True
        
    return False

# Получение секрета пользователя
async def get_reckey(login: str) -> bytes:
    async with get_async_session() as session:
        sql_query = \
            select(
                User.secret
            ).filter(
                User.login == login
            )
        key = (await session.execute(sql_query)).scalars().first()

    return key[0][0]

# смена пароля (восстановление)
async def change_passwd(login: str, password: str) -> None:
    async with get_async_session() as session:
        login_cleaned = delete_special_symbol(login)
        change_profile_query = text("ALTER USER :username WITH PASSWORD :password")
        await session.execute(
            change_profile_query,
            {"username": login_cleaned, "password": password}
        )
        encrypted_password = encrypt_create(
            key_recovery(setting.DB_USER, setting.DB_PASS, login_cleaned), password
        )
        update_user_query = (
            update(
                User
            ).where(
                User.login == login
            ).values(
                passwd=encrypted_password[1], initial_passwd=encrypted_password[0]
            )
        )

        await session.execute(update_user_query)
        await session.commit()

# Получение ключа для восстановления пароля
async def key_recovery(user: str, user_passwd: str, login: str) -> bytes:
    session = create_session(user, user_passwd)
    query = \
        select(
            User.key_crypt
        ).filter(
            User.login == login
        )
    result = await session.execute(query)
    key = result.scalar()

    return key

# Проверка лоигна при восстановлении 
async def check_user(log: str) -> bool:
    async with get_async_session() as session:
        cleaned_log = delete_special_symbol(log)
        query = text("SELECT rolname FROM pg_roles WHERE rolname = :log")
        result = await session.execute(query, {"log": cleaned_log})
        user = result.scalars().first()

        return user is not None

# Проверка количества неверных попыток
async def check_ban(login: str) -> Union[int, bool]:
    async with get_async_session() as session:
        query = \
            select(
                Ban.count
            ).filter(
                Ban.login == login
            )
        result = await session.execute(query)
        user_ban_count = result.scalar()

        if user_ban_count is not None:
            return user_ban_count
        else:
            return False

# Обновление неудачных попыток в БД
async def ban_record(login: str) -> None:
    async with get_async_session() as session:
        user_ban_count = await check_ban(login)

        if user_ban_count:
            stmt = (
                update(
                    Ban
                ).where(
                    Ban.login == login
                ).values(
                    count=user_ban_count + 1, email=0, time=get_time()
                )
            )
            await session.execute(stmt)
        else:
            stmt = \
                insert(
                    Ban
                ).values(
                    login=login, count=1, email=0, time=get_time()
                )
            await session.execute(stmt)

        await session.commit()

# Получение времени бана
async def get_timeban(login: str) -> Union[tuple[str], bool]:
    async with get_async_session() as session:
        query = \
            select(
                Ban.time,
                Ban.email
            ).filter(
                Ban.login == login
            )
        result = await session.execute(query)
        user_ban = result.first()
        
        if user_ban:
            return str(user_ban[0] + timedelta(hours=1)), user_ban[1]
        else:
            return False

# Обновление попыток при нахождении в бане
async def update_count(login: str) -> None:
    async with get_async_session() as session:
        current_count = await check_ban(login)
        
        if current_count:
            stmt = (
                update(
                    Ban
                )
                .where(
                    Ban.login == login
                ).values(
                    count = current_count + 1
                )
            )

            await session.execute(stmt)
            await session.commit()

# Установка email столбца в 1 для проверки статуса отправки письма
async def email_deliver(login: str) -> None:
    async with get_async_session() as session:
        stmt = (
            update(
                Ban
            ).where(
                Ban.login == login
            ).values(
                email = 1
            )
        )

        await session.execute(stmt)
        await session.commit()

# создание пользователя postgresql
async def create_acc_postgres(login: str, passwd: str) -> None:
    async with get_async_session() as session:
        # Составляем SQL-запрос с использованием text()
        query = """
        CREATE USER :login WITH PASSWORD :passwd;
        GRANT CONNECT ON DATABASE postgres TO :login;
        GRANT SELECT ON TABLE users TO :login;
        GRANT INSERT ON TABLE users TO :login;
        GRANT DELETE ON TABLE users TO :login;
        GRANT SELECT ON TABLE repository TO :login;
        GRANT INSERT ON TABLE repository TO :login;
        GRANT DELETE ON TABLE repository TO :login;
        GRANT UPDATE ON TABLE repository TO :login;
        GRANT USAGE ON SEQUENCE repository_id_seq TO :login;
        """

        await session.execute(
            text(query),
            {"login": login, "passwd": passwd}
        )
        
        await session.commit()

# создание сессии для выполнения запросов ORM
async def create_session(login: str, passwd: str) -> Union[AsyncSession, bool]:
    login = delete_special_symbol(login)

    engine = create_async_engine(
        f"postgresql+asyncpg://{login}:{passwd}@"\
        f"{setting.DB_HOST}:{setting.DB_PORT}/{setting.DB_NAME}",
        echo=True
    )
    
    Session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    try:
        async with engine.connect() as connection:
            await connection.scalar(select(1))
        session = Session()
        return session
    except Exception:
        return False

# создание аккаунта (создание Postgresql + записи в User)
async def save_account(image_path: str, log: str, password: str,
                       secret: str, key: bytes) -> None:
    async with get_async_session() as session:
        with Image.open(image_path) as img:
            img_byte_array = BytesIO()
            img.save(img_byte_array, format=img.format)
            img_byte_array = img_byte_array.getvalue()
        
        init_passwd = encrypt_create(key, password)
        
        new_data = User(
            login=log,
            passwd=init_passwd[1],
            secret=secret,
            photo=img_byte_array,
            key_crypt=key,
            initial_passwd=init_passwd[0]
        )
        
        session.add(new_data)

        await session.commit()
        await create_acc_postgres(log, password)

# экспорт фото для сравнения при входе (faceid)
async def export_photo(login: str, password: str) -> None:
    session = create_session(login, password)
    photo = await session.execute(
        select(User.photo).filter(User.login == login)
    )
    photo_data = photo.scalars().first()

    if photo_data:
        img_byte_array = BytesIO(photo_data)
        img = Image.open(img_byte_array)
        img.save("database_input_photo.jpg")
        img.close()

# список всех сервисов пользователя
async def count_note(login: str, password: str, key: bytes) -> Union[list[tuple], bool]:
    session = create_session(login, password)
    list_note = []
    list_iv = []

    query_id_result = await session.execute(
        select(User.id).filter(User.login == login)
    )
    query_id = query_id_result.scalars().first()

    if query_id:
        services_result = await session.execute(
            select(Repository).filter(Repository.user_id == query_id).order_by(Repository.id)
        )
        services = services_result.scalars().all()

        if services:
            for item in services:
                item.login = decrypt(key, item.initial_log, item.login)
                item.passwd = decrypt(key, item.initial_passwd, item.passwd)
                list_note.append([item.service, item.login, item.passwd, item.description])
                list_iv.append((item.initial_log, item.initial_passwd))

            return list_note, list_iv
        else:
            return False, False
    
# Расшифровка логина и пароля для их + сервиса отображения в списке сервисов    
async def get_decrypt_serlog(login: str, password: str, key: bytes) -> Union[list, bool]:
    session = create_session(login, password)
    list_data = []
    list_serlogpas = []
    query_id_result = await session.execute(
        select(User.id).filter(User.login == login)
    )
    query_id = query_id_result.scalars().first()

    if query_id:
        services_result = await session.execute(
            select(Repository).filter(Repository.user_id == query_id)
        )
        services = services_result.scalars().all()

        if services:
            for item in services:
                item.login = decrypt(key, item.initial_log, item.login)
                item.passwd = decrypt(key, item.initial_passwd, item.passwd)
                list_data.append([item.service, item.login])
                list_serlogpas.append([item.service, item.login, item.passwd])

            return list_data, list_serlogpas
        else:
            return False
    
# добавление новой записи в менеджере
async def make_note(key: bytes, user: str, user_passwd: str, resource: str,
                    log: str, password: str, descript: str) -> None:
    session = create_session(user, user_passwd)
    query_id_result = await session.execute(
        select(User.id).filter(User.login == user)
    )
    query_id = query_id_result.scalars().first()
    if query_id:
        iv_log, encrypt_log = encrypt_create(key, log)
        iv_passwd, encrypt_passwd = encrypt_create(key, password)
        new_data = Repository(
            user_id=query_id,
            service=resource,
            login=encrypt_log,
            passwd=encrypt_passwd,
            description=descript,
            initial_log=iv_log,
            initial_passwd=iv_passwd
        )

        session.add(new_data)
        await session.commit()

# удаление записи в repository
async def remove_note(user: str, user_passwd: str, service: str, \
                      login: str, key: bytes, iv: str) -> None:
    session = create_session(user, user_passwd)
    encrypted_login = encrypt_delete(key, login, iv)
    await session.execute(
        select(Repository).filter(
            Repository.service == service,
            Repository.login == encrypted_login
        ).delete()
    )
    await session.commit()

async def update_note(user: str, user_passwd: str, service: str, login: str, \
                      key: bytes, iv: str, password: str, description: str) -> None:
    session = create_session(user, user_passwd)
    encrypted_login = encrypt_delete(key, login, iv)
    iv_passwd, encrypted_passwd = encrypt_create(key, password)
    result = await session.execute(
        select(Repository).filter(
            Repository.service == service,
            Repository.login == encrypted_login
        )
    )
    record = result.scalars().first()
    if record:
        record.passwd = encrypted_passwd
        record.description = description
        record.initial_passwd = iv_passwd
        await session.commit()

# выделение строки для ее изменения
async def select_data(user: str, user_passwd: str, service: str, login: str, \
                        key: bytes, iv_log: str, iv_passwd: str) -> list[int]:
    session = create_session(user, user_passwd)
    encrypted_login = encrypt_delete(key, login, iv_log)
    result = await session.execute(
        select(Repository.passwd, Repository.description).filter(
            Repository.service == service,
            Repository.login == encrypted_login
        )
    )
    query = result.all()
    list_data = []
    for item in query:
        decrypted_passwd = decrypt(key, iv_passwd, item[0])
        list_data.append([decrypted_passwd, item[1]])
    return list_data[0] if list_data else []

# получение ключа пользователя
async def get_key(user: str, user_passwd: str) -> bytes:
    session = create_session(user, user_passwd)
    result = await session.execute(
        select(User.key_crypt).filter(User.login == user)
    )
    key = result.scalars().first()
    return key