from fastapi import APIRouter

# 创建 APIrouter 实例
# prefix 参数用于设置路由的前缀，tags 参数用于设置路由的标签
router = APIRouter(prefix="/api/news", tags=["news"])


@router.get("/categories")
async def get_categories():
    return {"message": "获取新闻分类成功"}
