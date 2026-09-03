from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.users import User
from schemas.users import UserRequest
from utils.security import get_password_hash


# 根据用户名查询数据库
async def get_user_by_username(db: AsyncSession, username: str):
    query = select(User).where(User.username == username)
    result = await db.execute(query)
    return result.scalar_one_or_none()


# 创建用户
async def create_user(db: AsyncSession, user_data: UserRequest):
    # 先密码加密 -> 再存入数据库
    hashed_password = get_password_hash(user_data.password)
    user = User(username=user_data.username, hashed_password=hashed_password)
    db.add(user)
    await db.commit()
    await db.refresh(user)  # 从数据库读回最新的 user 数据
    return user
