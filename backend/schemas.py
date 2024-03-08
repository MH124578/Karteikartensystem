from pydantic import BaseModel
from typing import Optional, List

class UserBase(BaseModel):
    username: str
    email: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(BaseModel):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

class FlashcardBase(BaseModel):
    question: str
    answer: str
    category_id: int

class FlashcardCreate(FlashcardBase):
    category_id: int


class Flashcard(FlashcardBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    flashcards: List[Flashcard] = []

    class Config:
        from_attributes = True