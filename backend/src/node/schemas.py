from datetime import datetime, timezone
from typing import Optional, List, Dict

from pydantic import BaseModel


class NodeBase(BaseModel):
    url: Optional[str]
    module: Optional[str]
    component: Optional[str]
    page: Optional[str]
    slug: Optional[bool] = False
    title: Optional[str]
    sub_title: Optional[str]
    description: Optional[str]
    keywords: Optional[str]
    robots: Optional[bool]
    canonical_full_url: Optional[str]
    user_role_id: Optional[int]
    user_auth: Optional[bool]
    name_menu: Optional[str]
    icon: Optional[str]

    class Config:
        orm_mode = True


class NodeRead(NodeBase):
    id: int


class NodeResponseRead(BaseModel):
    status: str
    data: NodeRead
    message: str


class NodesResponseRead(BaseModel):
    status: str
    data: list[NodeRead]
    message: str


class NodeResponseUpdate(BaseModel):
    status: str
    data: NodeBase = None
    message: str
