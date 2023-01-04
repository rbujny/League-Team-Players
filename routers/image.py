import shutil
from os.path import isfile
from fastapi import UploadFile, File, HTTPException, status


def upload_image(type_of_dir: str,image: UploadFile = File(...)):
    path = f"images/{type_of_dir}/{image.filename}"
    if isfile(path):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="There is already img with name like this.")
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": path}
