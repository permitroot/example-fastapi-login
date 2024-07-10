from fastapi import APIRouter
from starlette.responses import RedirectResponse

router = APIRouter()


@router.get("/")
async def redirect_redoc():
    return RedirectResponse(url='/redoc')
