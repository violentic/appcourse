from typing import List

from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import  asc

from app import models, schemas
from ..database import engine, SessionLocal, get_db

router = APIRouter(tags=['events'])


@router.get('/events', response_model=schemas.EventsResponse)
def get_events(db: Session = Depends(get_db)):
    posts = db.query(models.Events).order_by(asc(models.Events.id)).all()
    response = schemas.get_events_response(posts)

    return response
