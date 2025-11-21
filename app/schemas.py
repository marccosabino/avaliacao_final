from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class ItemCreate(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None


class RatingCreate(BaseModel):
    user_id: int
    item_id: int
    rating: float