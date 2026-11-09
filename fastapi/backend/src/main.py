from fastapi import FastAPI

from src.api.posts import router as posts_router
from src.api.users import router as users_router
from src.core.config import APP_TITLE
from src.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title=APP_TITLE)
app.include_router(posts_router)
app.include_router(users_router)


@app.get("/")
def root():
    return {"message":"hello world"}