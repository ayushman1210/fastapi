
from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime

class Postmodel(BaseModel):
    Title:str
    Content:str
    published: bool=True



class PostCreate(Postmodel):
    pass


class user_response(BaseModel):
    id:int
    email:EmailStr    
    created_at:datetime


class Postresponse(BaseModel):
    Title:str
    Content:str
    published:bool
    owner:user_response
    class Config:
        orm=True


class Createpost(Postmodel):
    pass

# class Postresponse(Postmodel):
#     id:int
#     created_at:datetime
#     owner_id:int
#     class Config:
#         orm=True


class user_created(BaseModel):
    email:EmailStr
    password:str



class user_login(user_created):
    pass


class token(BaseModel):
    acess_token:str
    token_type:str


class tokendata(BaseModel):
    id:Optional[str]
        