from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from .config import Settings

engine=create_async_engine(Settings.Database_url,echo=True)


AsyncSessionfactory=sessionmaker(engine,class_=AsyncSession, expire_on_commit=False)


async def get_session():
    async with AsyncSessionfactory() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
        finally:
            await session.close()        