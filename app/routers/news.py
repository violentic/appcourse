from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from .. import schemas, models, utils, oauth2, database

router = APIRouter(tags=['news'])


@router.get('/news', response_model=schemas.NewsResponse)
def get_news(db: Session = Depends(database.get_db)):
    posts = db.query(models.News).all()
    response = schemas.get_news_response(posts)

    return response