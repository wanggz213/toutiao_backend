from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.db_conf import get_db

# 创建 APIrouter 实例
# prefix 参数用于设置路由的前缀，tags 参数用于设置路由的标签
router = APIRouter(prefix="/api/news", tags=["news"])


@router.get("/categories")
async def get_categories(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    categories = await get_categories(db, skip=skip, limit=limit)
    return {
        "code": 200,
        "message": "success",
        "data": categories
    }
