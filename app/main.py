import shutil
import io
##
from fastapi import FastAPI, Response, status, HTTPException, APIRouter, UploadFile, File

from fastapi.responses import FileResponse
from .routers import books, news, events, images, users, auth, upload_assets
from . import models, schemas
from .database import engine
from app import database
from .config import Settings

app = FastAPI()


models.Base.metadata.create_all(bind=engine)


app.include_router(events.router)
app.include_router(books.router)
app.include_router(news.router)

app.include_router(images.router)
app.include_router(upload_assets.router)

app.include_router(users.router)
app.include_router(auth.router)




@app.get("/")
def root():
    return {"message": "hello worlds"}

