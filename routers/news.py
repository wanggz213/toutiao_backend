from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from config.db_conf import get_db
from crud import news

# 创建 APIrouter 实例
# prefix 参数用于设置路由的前缀，tags 参数用于设置路由的标签
router = APIRouter(prefix="/api/news", tags=["news"])


@router.get("/categories")
async def get_categories(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    categories = await news.get_categories(db, skip=skip, limit=limit)
    return {
        "code": 200,
        "message": "success",
        "data": categories
    }


# 添加获取新闻列表路由
@router.get("/list")
async def get_news_list(
        category_id: int = Query(..., alias="categoryId"),
        page: int = 1,
        page_size: int = Query(10, alias="pageSize", le=100),
        db: AsyncSession = Depends(get_db)
):
    # 思路：处理分页规则 -> 查询新闻列表 -> 计算总量 -> 计算是否还有更多
    offset = (page - 1) * page_size
    news_list = await news.get_news_list(db, category_id, skip=offset, limit=page_size)
    total = await news.get_news_count(db, category_id)
    # (跳过的 + 当前列表里边的数量) < 总量 → 还有更多
    has_more = (offset + len(news_list)) < total
    return {
        "code": 200,
        "message": "success",
        "data": {
            "list": news_list,
            "total": total,
            "hasMore": has_more
        }
    }
