from fastapi import APIRouter
from starlette import status


router = APIRouter(prefix="/healthcheck")


@router.get("", status_code=status.HTTP_200_OK)
async def healthcheck():
    return {"healthcheck": "success"}
