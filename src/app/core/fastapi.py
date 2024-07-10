from fastapi.applications import FastAPI
from fastapi.exceptions import HTTPException, RequestValidationError

from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from ..common.settings import Settings
from ..api.routers.router_root import router as router_root
from ..api.routers.router_v1 import router as router_api_v1

from .schemas import (
    CommonError, CommonErrorError, AppRequestValidationError,
    AppRequestValidationErrorError
)


def add_exception_handlers(app):
    @app.exception_handler(HTTPException)
    async def app_exception_handler(request: Request, exc: HTTPException):
        content = CommonError(
            error=CommonErrorError(
                detail_code=exc.__class__.__name__,
                detail=exc.detail))

        return JSONResponse(
            status_code=exc.status_code,
            content=content.dict()
        )

    @app.exception_handler(RequestValidationError)
    async def request_validation_handler(request: Request, exc: RequestValidationError):
        content = AppRequestValidationError(
            error=AppRequestValidationErrorError(
                detail_code=RequestValidationError.__name__,
                detail=exc.errors()
            )
        )
        return JSONResponse(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            content=content.dict()
        )


def get_application(settings: Settings) -> FastAPI:
    _app = FastAPI(title=settings.project_name,
                   responses={'400': {"model": CommonError},
                              '422': {"model": AppRequestValidationError},
                              '500': {"model": CommonError}},
                   routes=settings.routes
                   )

    if settings.backend_cors_origins:
        _app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.backend_cors_origins],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    _app.include_router(router_root, prefix="")
    _app.include_router(router_api_v1, prefix="/api")

    add_exception_handlers(_app)

    return _app
