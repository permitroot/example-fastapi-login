from fastapi import APIRouter

from .ex1.example import router as ex1_example


router = APIRouter(prefix="/example")


router.include_router(ex1_example)
