from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    categories = relationship('Category', back_populates='user')
    flashcards = relationship('Flashcard', back_populates='owner')

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='categories')
    flashcards = relationship('Flashcard', back_populates='category')

class Flashcard(Base):
    __tablename__ = "flashcards"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)
    answer = Column(Text)
    category_id = Column(Integer, ForeignKey('categories.id'))  # Fremdschlüsselbeziehung zur Category-Tabelle
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship('User', back_populates='flashcards')
    category = relationship('Category', back_populates='flashcards')
