from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from db.connection import async_session


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
        except:
            await session.rollback()
