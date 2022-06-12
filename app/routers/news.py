from fastapi import APIRouter, HTTPException, Depends, status, Response
from sqlalchemy.orm import Session

from .. import schemas, models, utils, oauth2, database
from ..database import engine, SessionLocal, get_db

router = APIRouter(tags=['news'])


@router.get('/news', response_model=schemas.NewsResponse)
def get_news(db: Session = Depends(database.get_db)):
    posts = db.query(models.News).all()
    response = schemas.get_news_response(posts)

    return response

@router.post('/news/add', status_code=status.HTTP_201_CREATED, response_model=schemas.CreateNews)
def create_news(news: schemas.NewsModel, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):  # save as pydantic model
   
    new_post = models.News(**news.dict())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.delete('/news/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_news(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    print(id)
    deleted_post = db.query(models.News).filter(models.News.id == id)

    if deleted_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found')

    deleted_post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@ router.put('/news/update/{id}', response_model=schemas.CreateNews)
def update_news(id: int, news: schemas.NewsModel, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
   
    post_queury = db.query(models.News).filter(models.News.id == id)
    updated_post = post_queury.first()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found')

    news = news.dict()
    news['id'] = id
    news['updated_at'] = updated_post.updated_at
    post_queury.update(news, synchronize_session=False)
    db.commit()

    return post_queury.first()