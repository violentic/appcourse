from typing import List

from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import  asc

from app import models, schemas, oauth2
from ..database import engine, SessionLocal, get_db

router = APIRouter(tags=['events'])


@router.get('/events', response_model=schemas.EventsResponse)
def get_events(db: Session = Depends(get_db)):
    posts = db.query(models.Events).order_by(asc(models.Events.id)).all()
    response = schemas.get_events_response(posts)

    return response


@router.post('/event/add', status_code=status.HTTP_201_CREATED, response_model=schemas.CreateEvent)
def create_event(event: schemas.EventModel, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):  # save as pydantic model
   
    new_post = models.Events(**event.dict())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.delete('/event/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_event(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    deleted_post = db.query(models.Events).filter(models.Events.id == id)

    if deleted_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found')

    deleted_post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@ router.put('/event/update/{id}', response_model=schemas.CreateEvent)
def update_event(id: int, event: schemas.EventModel, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
   
    post_queury = db.query(models.Events).filter(models.Events.id == id)
    updated_post = post_queury.first()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found')

    event = event.dict()
    event['id'] = id
    post_queury.update(event, synchronize_session=False)
    db.commit()

    return post_queury.first()