import logging.config

from src.app.common.schemas import Example
from src.app.common.variables import config_log

logging.config.dictConfig(config_log)
logger = logging.getLogger(__name__)


async def execute():
    return Example(example="example")
