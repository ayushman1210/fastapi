from typing import List,Optional
from sqlmodel import Field,Relationship,SQLModel

class user(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    username:str=Field(index=True, unique=True)
    password:str
    role:str="customer"
    reviews=List["review"]=Relationship(back_populates="user")

class product(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    name:str=Field(index=True)
    description:str
    price:float
    category:"category"=Relationship(back_populates="product")
    reviews=List["review"]=Relationship(back_populates="product")


class category(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    name:str=Field(index=True, unique=True)
    products=List["product"]=Relationship(back_populates="category")

class review(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    text:str
    rating:int

    user_id=int=Field(foreign_key="user.id")
