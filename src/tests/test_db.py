from database import get_async_session


# Методы для тестов
async def check():
    async with get_async_session() as session:
        sql_query = "SELECT rolname FROM pg_roles;"
        users = (await session.execute(sql_query)).scalars().all()
        print("Список пользователей PostgreSQL:")
        for user in users:
            print(user[0])

async def delete():
    async with get_async_session() as session:
        query_db = "REVOKE ALL PRIVILEGES ON DATABASE postgres FROM komarkostyabkru;"
        query_t = "REVOKE ALL PRIVILEGES ON TABLE users, repository FROM komarkostyabkru;"
        sql_query = "DROP ROLE komarkostyabkru;"
        x = "REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM komarkostyabkru;"
        y = "REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public FROM komarkostyabkru;"
        await session.execute(query_db)
        await session.execute(query_t)
        await session.execute(x)
        await session.execute(y)
        await session.execute(sql_query)
        await session.commit()
