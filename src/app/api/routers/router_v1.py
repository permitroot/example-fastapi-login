from fastapi import APIRouter

from .v1.router_example import router as example_router
from .v1.router_healthcheck import router as healthcheck_router


router = APIRouter(prefix="/v1")

router.include_router(example_router, tags=["example"])
router.include_router(healthcheck_router, tags=["healthcheck"])
