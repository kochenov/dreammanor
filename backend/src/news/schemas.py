from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field


class Category(BaseModel):
    id: int
    name: str


class NewCategory(BaseModel):
    name: str


class PostCreate(BaseModel):
    id: int
    title: str
    category_id: Optional[int]
    category: Optional[Category] | None = None
    content: str
    short_description: Optional[str]
    created_ad: Optional[datetime] | None = datetime.utcnow()
    count_views: Optional[int]


class PostCreateAd(BaseModel):
    title: str
    category_id: int
    short_description: str
    content: str


class ViewNews(BaseModel):
    status: str
    data: PostCreate
    details: str | None = None


class PostRead(PostCreate):
    category: Optional[Category] = None
