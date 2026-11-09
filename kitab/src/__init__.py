from fastapi import FastAPI
from contextlib import asynccontextmanager 
from src.books.routes import book_router
from src.db.main import init_db


@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"server is going to start ")
    await init_db()
    yield
    print(f"server is going to stopped")


version="v1"

app=FastAPI(title="Kitab Microservices", description="a app based on locating books seller and consumer",version=version,lifespan=life_span)


app.include_router(book_router,prefix=f"/api/{version}/books",tags=["books"])