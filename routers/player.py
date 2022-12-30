from fastapi import APIRouter

router = APIRouter(
    prefix="/player",
    tags=["player"]
)