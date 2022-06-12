from typing import List
#
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
#
from app import models, schemas, oauth2
from ..database import engine, SessionLocal, get_db

router = APIRouter(tags=['books'])


@router.get('/books/new', response_model=schemas.BookResponse)
def get_books(db: Session = Depends(get_db)):
    posts = db.query(models.Books).all()
    response = schemas.get_book_response(posts)

    return response


@router.post('/books/add', status_code=status.HTTP_201_CREATED, response_model=schemas.CreateBook)
def create_book(book: schemas.BookModel, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):  # save as pydantic model
   
    new_post = models.Books(**book.dict())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.delete('/books/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    deleted_post = db.query(models.Books).filter(models.Books.id == id)

    if deleted_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found')

    deleted_post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@ router.put('/books/update/{id}', response_model=schemas.CreateBook)
def update_post(id: int, book: schemas.BookModel, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
   
    post_queury = db.query(models.Books).filter(models.Books.id == id)
    updated_post = post_queury.first()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found')

    book = book.dict()
    book['id'] = id
    book['created_at'] = updated_post.created_at
    post_queury.update(book, synchronize_session=False)
    db.commit()

    return post_queury.first()

