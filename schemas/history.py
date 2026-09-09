from pydantic import BaseModel, Field


class HistoryAddRequest(BaseModel):
    """
    添加历史记录请求
    """
    news_id: int = Field(..., alias="newsId")
