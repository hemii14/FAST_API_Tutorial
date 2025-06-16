from typing import List, Optional
from pydantic import BaseModel


# For blog creation
class Blog(BaseModel):
    title: str
    body: str
    user_id: int

    class Config:
        from_attributes = True


# For showing blog inside a user
class BlogInUser(BaseModel):
    title: str
    body: str

    class Config:
        from_attributes = True


# For user creation
class User(BaseModel):
    name: str
    email: str
    password: str


# For showing user with blogs
class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[BlogInUser] = []

    class Config:
        from_attributes = True


# For showing blog with its creator (user)
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config:
        from_attributes = True


# schemas.py


class Login(BaseModel):
    username: str
    password: str  # optional for now



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
