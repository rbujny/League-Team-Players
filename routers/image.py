import shutil

from fastapi import UploadFile, File


def upload_image(image: UploadFile = File(...)):
    path = f"images/{image.filename}"
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": path}
