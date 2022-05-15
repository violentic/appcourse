from typing import List

from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from app import models, schemas
from ..database import engine, SessionLocal, get_db

router = APIRouter(tags=['books'])


@router.get('/books/new', response_model=schemas.BookResponse)
def get_books(db: Session = Depends(get_db)):
    posts = db.query(models.Books).all()
    response = schemas.get_book_response(posts)

    return response
