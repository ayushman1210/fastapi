# from fastapi import FastAPI,status,Body,Depends,Header,HTTPException
# from pydantic import BaseModel,validate_call,ValidationError,StringConstraints,Field
# from typing import Optional
# from typing import Annotated
# app=FastAPI()


# class itemdata(BaseModel):
#     name:str=Field(... ,min_length=4) 
#     price:int | None=None
#     discount:Optional[int]=None



# post:list[dict]=[
#     {
#         "id":1,
#         "name":"lets go ",
#         "title":"the book that we need",
#         "author":"ayushman"
#     },
#      {
#             "id":2,
#             "name":"lets go two ",
#             "title":"the book that we need for 2 ",
#             "author":"ayushman1"
#         },
#          {
#                 "id":3,
#                 "name":"lets go three ",
#                 "title":"the book that we need for three",
#                 "author":"ayushman12"
#             }
# ]


# class offer(BaseModel):
#     offer:int    

# @validate_call
# def validate(name:Annotated[str,StringConstraints(min_length=6)]):
#  return name

# try:
# #    name=validate(name="ayushm")
#     product=itemdata(name="item1",price=12)
#     product_detail=product.model_dump(exclude={'price'})
#     print("name is valid",product_detail)
# except ValidationError as error:
#     print("error",error)


# @app.get('/',status_code=status.HTTP_200_OK)
# async def startup(): 
#     return{"message":"build is done"}


# @app.post('/item')
# async def get_item(item:itemdata):
#     return item
# @app.get('/{itemdata}')
# async def item_show(itemdata:str,q:str|None=None):
#     return {"data":itemdata,"q":q}


# @app.post('/items', include_in_schema=False)
# async def get_items(item:itemdata, 
#                      offer:offer,
#                      extra:Annotated[str,Body()]):
#     return {"item":item,"offer":offer,"extra":extra}



# async def get_db_session():
#     print('db session i got')
#     session={1:"successs",2:{"true":"false"}}
#     try:
#         yield session
#     finally:
#         print("hello world ")    



# Db_session=Annotated[dict,Depends(get_db_session)]

# async def get_user(token:Annotated[str| None, Header]):
#     print("checking auth")
#     user={"userneame":"test_user"}
#     return user

# # current_user=Annotated[dict,Depends[get_db_session]]

# # @app.get('/data')
# # async def hello_data(db:Db_session, user:current_user):
# #     pass    


# @app.get('/post/{post_id}',status_code=status.HTTP_200_OK)
# async def get_post(post_id:int):
#     for posts in post:
#         if posts.get("id")==post_id:
#             return post

#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"this post is not available {post_id}")



from fastapi import FastAPI

from api import user,product,category,review



app=FastAPI()

app.include_router(user.router,prefix="/api/v1/users",tages=["user"])
app.include_router(product.router,prefix="/api/v1/product",tages=["product"])
app.include_router(category.router,prefix="/api/v1/category",tages=["category"])
app.include_router(review.router,prefix="/api/v1/review",tages=["review"])













