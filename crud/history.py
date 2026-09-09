from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.history import History


async def add_history(db: AsyncSession, user_id: int, news_id: int):
    """
    添加历史记录
    """
    query = select(History).where(History.user_id == user_id, History.news_id == news_id)
    result = await db.execute(query)
    existing_history = result.scalar_one_or_none()
    if existing_history:
        existing_history.view_time = datetime.now()
        await db.commit()
        await db.refresh(existing_history)
        return existing_history
    else:
        new_history = History(user_id=user_id, news_id=news_id, view_time=datetime.now())
        db.add(new_history)
        await db.commit()
        await db.refresh(new_history)
        return new_history
