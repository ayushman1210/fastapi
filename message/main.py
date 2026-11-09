from fastapi import FastAPI,BackgroundTasks
from pydantic import BaseModel,validate_call,ValidationError,StringConstraints,Field
from typing import Optional,Annotated
import time
app=FastAPI()


class Item(BaseModel):
    name:str=Field(...,min_length=4)
    price: float
    description:str |None=None
    tax:Optional[float]=None

class Offer(BaseModel):
    offer:str  

@app.get('/')
async def get_health():
    return {"message":"hello world"}


@app.get("/api/{item_name}")
async def get_data(item_name:str, q:str|None=None):
    return {"item name":item_name,"q":q}


@app.get("/api/data/items")
async def all_item(skip:int=0, limit:int=3):
    dummy_data=[
        {"name":"lap1","price":100},
        {"name":"lap2","price":200},
        {"name":"lap3","price":300},
        {"name":"lap4","price":400},
        {"name":"lap5","price":500},
    ]
    return dummy_data[skip:skip+limit]


# @validate_call
# def validate_name(name:Annotated[str,StringConstraints(min_length=4)]):
#     return name 



try:
   product=Item(name="ayush",price=100.01)
   product_without_price=product.model_dump(exclude={'price'})
   print(product_without_price)
except  ValidationError as error:
    print("name is invalid {error}")        




@app.post('/item')
async def create_item(item:Item, offer:Offer):
    return {"item":item, "offer":offer}    

def write_log(message:str):
    print(f"Background task:{message}")
    with open("log.txt", mode="a") as log:
        log.write(f"{message}\n")

def send_notification(email:str,message:str):
    BackgroundTasks.add

