from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: Optional[str]


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class EmailSchema(BaseModel):
    email: EmailStr
