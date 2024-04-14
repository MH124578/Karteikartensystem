from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Willkommen zur FastAPI Anwendung!"}

@app.post("/create_users", response_model=schemas.User)
def create_new_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/login")
def login(login_data: schemas.Login, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email=login_data.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.hashed_password != login_data.password:
        raise HTTPException(status_code=400, detail="Incorrect password")
    return {"message": "Login successful!", "user_id": user.id} 

@app.post("/users/{user_id}/flashcards")
def create_flashcard_for_user(user_id: int, flashcard: schemas.FlashcardCreate, db: Session = Depends(get_db)):
    return crud.create_user_flashcard(db=db, flashcard=flashcard, user_id=user_id, category_id=flashcard.category_id)

@app.post("/users/{user_id}/categories", response_model=schemas.Category)
def create_category_for_user(
    user_id: int, 
    category: schemas.CategoryCreate, 
    db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category, user_id=user_id)

@app.get("/users/{user_id}/categories")
def get_categories_for_user(
    user_id: int, 
    db: Session = Depends(get_db)):
    return crud.get_categories(db=db, user_id=user_id)

@app.get("/flashcards", response_model=List[schemas.Flashcard])
def get_flashcards(category_id: int, db: Session = Depends(get_db)):
    flashcards = crud.get_flashcards_by_category(db, category_id=category_id)
    if not flashcards:
        raise HTTPException(status_code=404, detail="No flashcards found for the given category")
    return flashcards

@app.delete("/categories/{category_id}")
def delete_category(
    category_id: int, 
    db: Session = Depends(get_db)):
    crud.delete_category(db=db, category_id=category_id)
    return {"status": "ok"}

@app.options("/create_users", response_model=None)
def login_options():
    return {}