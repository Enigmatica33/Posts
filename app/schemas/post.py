from pydantic import BaseModel, ConfigDict, constr
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: constr(max_length=200)
    content: str


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: Optional[constr(max_length=200)] = None
    content: Optional[str] = None


class PostResponse(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
