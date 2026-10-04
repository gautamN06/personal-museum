from fastapi import APIRouter 
from sqlalchemy.orm import Session 

from app.db import engine 
from app.models import Book 
from app.schemas import BookCreate, BookResponse 

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate):
    with Session(engine) as session: 
        new_book = Book(
            title = book.title, 
            author = book.author,
            description = book.description,
            rating = book.rating, 
            personal_notes = book.personal_notes,
        )

        session.add(new_book)
        session.commit()
        session.refresh(new_book)

        return new_book 
