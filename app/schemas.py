from datetime import datetime
from typing import Optional, List
#
from pydantic import BaseModel
from pydantic import EmailStr

## news schema

class NewsModel(BaseModel):
    id: int
    image: str
    summary: str
    newsHeader: str
    author: str
    publicationDate: str
    updated_at: datetime
 
    class Config:
        orm_mode = True


class NewsResponse(BaseModel):
    news: List[NewsModel]


## events Schema
class EventModel(BaseModel):
    id: int
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



##BOOK
class BookModel(BaseModel):
    id: int
    bookAuthor: str
    bookName: str
    bookSummary: str
    imagePath: str
    rating: float
    textDirection: str
    tags: str
    created_at: datetime
    publicationDate: str
 
    class Config:
        orm_mode = True


class BookResponse(BaseModel):
    books: List[BookModel]



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
    phone: str
    f_name: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    phone: str
    f_name: str
   

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
