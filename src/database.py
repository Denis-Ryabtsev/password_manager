from typing import AsyncGenerator

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, \
                                    async_sessionmaker, \
                                    AsyncSession

from config import setting


a_engine = create_async_engine(
    url=setting.DB_URL,
    echo=True,
    pool_size=5,
    max_overflow=10
)

a_session = async_sessionmaker(a_engine)


class Base(DeclarativeBase):
    pass


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with a_session() as session:
        yield session