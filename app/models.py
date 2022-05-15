from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.sql.sqltypes import Date, TIMESTAMP
from sqlalchemy.sql.expression import text
#
from .database import Base


### News
class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True, nullable=False)
    image = Column(String, nullable=False)
    summary = Column(String, nullable=False)
    newsHeader = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publicationDate = Column(String,
                        nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

### Events
class Events(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, nullable=False)
    eventName = Column(String, nullable=False)
    eventType = Column(String, nullable=False)
    eventDetail = Column(String, nullable=False)
    eventColor = Column(String, nullable=False)
    location = Column(String, nullable=False)
    time = Column(String, nullable=False)
    month = Column(String, nullable=False)
    day = Column(String, nullable=False)
    imageURL = Column(String, nullable=False)


## BOOKS
class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, nullable=False)
    bookAuthor = Column(String, nullable=False)
    bookName = Column(String, nullable=False)
    bookSummary = Column(String, nullable=False)
    imagePath = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    textDirection = Column(String, nullable=False)
    tags = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    publicationDate = Column(String,
                        nullable=False)



