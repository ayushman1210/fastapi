from sqlmodel import SQLModel
import uuid
from datetime import datetime
from sqlmodel import Column,Field
import sqlalchemy.dialects.postgresql as pg


class User(SQLModel, table=True):
    __tablename__="user"
    uid:uuid.UUID=Field(sa_column=Column(
    pg.UUID,nullable=False,primary_key=True, default=uuid.uuid4))
    username:str
    email:str
    first_name:str
    last_name:str
    is_verfied:bool=False
    created_at:datetime
    updated_at:datetime


def __repr__(self):
    return f"User{self.username}"