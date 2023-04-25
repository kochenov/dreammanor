from datetime import datetime, timezone
from typing import Optional, List, Dict

from pydantic import BaseModel


class MenuItemBase(BaseModel):
    name: str
    url: str
    role_id: Optional[int] = 0
    parent_id: Optional[int] = 0
    status: Optional[bool] = False
    priority: Optional[int] = 0

    class Config:
        orm_mode = True


class MenuItemRead(MenuItemBase):
    id: int


class MenuItemResponseRead(BaseModel):
    status: str
    data: list[MenuItemRead] = None
    message: str


class MenuItemResponseUpdate(BaseModel):
    status: str
    data: MenuItemBase = None
    message: str
