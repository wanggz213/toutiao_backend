from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict

from schemas.base import NewsItemBase


class HistoryAddRequest(BaseModel):
    """
    添加历史记录请求
    """
    news_id: int = Field(..., alias="newsId")


class HistoryNewsItemResponse(NewsItemBase):
    """
    浏览历史列表中的新闻项响应
    """
    history_id: int = Field(alias="historyId")
    view_time: datetime = Field(alias="viewTime")

    # 模型类配置
    model_config = ConfigDict(
        populate_by_name=True,  # alias / 字段名兼容
        from_attributes=True  # 允许从 ORM 对象属性中取值
    )


class HistoryLiteResponse(BaseModel):
    """
    浏览历史列表响应
    """
    list: list[HistoryNewsItemResponse]
    total: int
    has_more: bool = Field(alias="hasMore")

    # 模型类配置
    model_config = ConfigDict(
        populate_by_name=True,  # alias / 字段名兼容
        from_attributes=True  # 允许从 ORM 对象属性中取值
    )
