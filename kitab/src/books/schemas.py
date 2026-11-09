from pydantic import BaseModel
from typing import List
from datetime import datetime,date
import uuid 

class Book(BaseModel):
    uid:uuid.UUID
    title:str
    author:str
    publisher:str
    published_date:date
    page_count:str
    language:str
    created_at:datetime

class bookCreateModel(BaseModel):
    title:str
    author:str
    publisher:str
    published_date:date
    page_count:int
    language:str

class BookUpdateModel(BaseModel):
    title:str
    author:str
    publisher:str
    page_count:str
    language:str

