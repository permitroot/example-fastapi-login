from .common.variables import settings
from .core.fastapi import get_application


app = get_application(settings=settings)
