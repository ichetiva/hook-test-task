from typing import Generic, TypeVar, Type, Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.base import Base

Model = TypeVar("Model", Base)


class BaseRepository(Generic[Model]):
    def __init__(self, model: Type[Model], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def get(self, for_update: bool = False, **kwargs) -> Model | None:
        stmt = select(self.model).filter_by(**kwargs)
        if for_update:
            stmt = stmt.with_for_update()
        instance = await self.session.scalar(stmt)
        return instance

    async def get_or_create(
        self,
        defaults: dict[str, Any] = {},
        for_update: bool = False,
        **kwargs,
    ) -> Model:
        instance = await self.get(for_update=for_update, **kwargs)
        if instance:
            return instance, False
        kwargs.update(defaults)
        instance = self.model(**kwargs)
        self.session.add(instance)
        return instance
