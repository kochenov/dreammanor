from datetime import datetime, timezone
from typing import Optional, List

from pydantic import BaseModel


class Status(BaseModel):
    id: int
    name: str


class LinkCreate(BaseModel):
    id: Optional[int]
    link: str
    status_id: Optional[int]
    comment: Optional[str]
    created_ad: Optional[datetime] | None = datetime.now(timezone.utc)


class LinkView(BaseModel):
    id: Optional[int]
    link: str
    created_ad: datetime


class LinkUpdate(BaseModel):
    status_id: int
    comment: Optional[str]


class ViewLinks(BaseModel):
    status: str
    data: List[LinkCreate]
    details: str | None = None
