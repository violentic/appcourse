
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.responses import FileResponse

import os.path

router = APIRouter(tags=['images'])


@router.get('/images/{imagePath}')
async def get_image(imagePath: str):
    path_to_file = f'./app/assets/images/{imagePath}'

    if not os.path.exists(path_to_file):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'file {imagePath} not found')

    return FileResponse(path_to_file)
