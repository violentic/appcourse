import shutil
import io
##
from fastapi import APIRouter, UploadFile, File, status

router = APIRouter(tags=['upload'])

@router.post("/uploadimage", status_code=status.HTTP_201_CREATED)
async def upload_image(file: UploadFile = File(...)):
    fdst = open(f'./app/assets/images/{file.filename}', 'wb')
    shutil.copyfileobj(file.file, fdst)
    fdst.close()
    print(file)
    
    return {'image': file.filename}
