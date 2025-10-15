from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime


# Item schemas
class ItemBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# User schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=100)


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    items: List[Item] = []

    class Config:
        from_attributes = True
