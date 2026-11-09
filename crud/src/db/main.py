from sqlmodel import create_engine,text

from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import config
from src.student.models import Students

engine=AsyncEngine(create_engine(
    url=config.DB_URL,
    echo=True

))


async def init__db():
    async with engine.begin() as conn:
        from src.student.models import Students
        