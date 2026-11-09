from typing import List,Optional

from sqlmodel import SQLModel

class categoryBase(SQLModel):
    pass


class category_public(categoryBase):
    pass

class UserBase(SQLModel):
    pass
class reviewBase(SQLModel):
    pass
class reviewPublic(reviewBase):
    pass

class ProductBase(SQLModel):
    name:str
    description:str
    price:float


class product_create(ProductBase):
    category_id:int

class ProductPublic(ProductBase):
    id:int
    category:category_public 
    review: List[reviewPublic] =[] 