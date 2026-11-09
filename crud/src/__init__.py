from fastapi import FastAPI
from src.student.routes import student_router
from contextlib import asynccontextmanager
from src.db.main import init__db

@asynccontextmanager
async def life_span(app:FastAPI):
    print('server is starting')
    await init__db()
    yield
    print("server has been stopped ")

version="v1"
app=FastAPI(
    title="suhi",
    description=" a rest api for suhi",
    version=version,
    lifespan=life_span
)

app.include_router(student_router,prefix=f"/{version}/student",tags=["students"])