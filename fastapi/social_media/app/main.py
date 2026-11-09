from fastapi import FastAPI


from passlib.context import CryptContext

from . import models
from .db import engine
from .router import user,post,auth


pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
models.Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


# @app.post('/')
# async def hello(payload:dict=Body(...)):
#     print(payload)
#     return payload






