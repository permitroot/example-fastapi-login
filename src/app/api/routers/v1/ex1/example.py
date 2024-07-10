import logging.config

from fastapi import APIRouter, HTTPException

from .....common.schemas import Example
from .....common.variables import config_log
from ....services.ex1.example import execute


logging.config.dictConfig(config_log)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/ex1")


@router.post("", response_model=Example)
async def example():
    result = await execute()
    logger.info(result)
    if isinstance(result, type(None)):
        raise HTTPException(status_code=404, detail="data not found")

    return result
