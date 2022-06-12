from datetime import datetime
from typing import Optional, List
#
from pydantic import BaseModel
from pydantic import EmailStr

## news schema

class NewsModel(BaseModel):
    id: Optional[int]
    image: str
    summary: str
    newsHeader: str
    author: str
    publicationDate: str
    updated_at: Optional[datetime]
 
    class Config:
        orm_mode = True


class NewsResponse(BaseModel):
    news: List[NewsModel]

class CreateNews(BaseModel):
    id: int
    newsHeader: str

    class Config:
        orm_mode = True    


## events Schema
class EventModel(BaseModel):
    id: Optional[int]
    eventName: str
    eventType: str
    eventDetail: str
    eventColor: str
    location: str
    time: str
    month: str
    day: str
    imageURL: str
 
    class Config:
        orm_mode = True


class EventsResponse(BaseModel):
    events: List[EventModel]

class CreateEvent(BaseModel):
    id: int
    eventName: str

    class Config:
        orm_mode = True    



##BOOK
class BookModel(BaseModel):
    id: Optional[int]
    bookAuthor: str
    bookName: str
    bookSummary: str
    imagePath: str
    rating: float
    textDirection: str
    tags: str
    created_at: Optional[datetime]
    publicationDate: str
 
    class Config:
        orm_mode = True





class BookResponse(BaseModel):
    books: List[BookModel]

class CreateBook(BaseModel):
    id: int
    bookName: str

    class Config:
        orm_mode = True



def get_news_response(news):
    return NewsResponse(news=news)


def get_events_response(events):
    return EventsResponse(events=events)


def get_book_response(books):
    return BookResponse(books=books)



## user creation
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
   
    class Config:
        orm_mode = True



## authentication

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str]
