from sqlmodel import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from sqlmodel import SQLModel
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession 


engine=AsyncEngine(create_engine(
url=Config.DATABASE_URL,
echo=True
))

async def init_db():
    async with engine.begin() as conn:
        from src.books.models import Book
        await conn.run_sync(SQLModel.metadata.create_all)



async def get_session()->AsyncSession:
    Session=sessionmaker(
        bind=AsyncEngine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session