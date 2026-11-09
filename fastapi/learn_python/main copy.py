from fastapi import FastAPI,Header,status
# from typing import Optional
from typing import List
from src.student.student_data import student
from src.student.schema import student_update,Students
from fastapi.exceptions import HTTPException
app=FastAPI()

# @app.get('/')
# async def hello():
#    return {"message":"hello server is up"}

# # @app.get('/greet/{name}')
# # async def greet(name:str)->dict:
# #    return {"name":name}


# # when no query is passed 

# @app.get('/greet/{name}')
# async def greet(name:str,age:int)->dict:
#    return {"message":f"hello {name} your age is {age}"}


# @app.get('/greet')
# async def greet(name:Optional[str]="User",age:int=0)->dict:
#    return {"message":f"hello {name} and age is {age}"}


# class healthModel(BaseModel):
#    Name:str
#    age:int
#    health:int 


# @app.post('/create',status_code=201)
# async def create(childhealth:healthModel):
#    return {
#       "Name":childhealth.Name,
#       "Age":childhealth.age,
#       "health":childhealth.health
#    }

# @app.get('/head',status_code=200)
# async def get_headers(accept:str=Header(None),content_type:str=Header(None),user_agent:str=Header(None),Host:str=Header(None)):
#    request_headers={}
#    request_headers["Accept"]=accept 
#    request_headers["content_type"]=content_type
#    request_headers["user_agent"]=user_agent
#    request_headers["Host"]=Host
#    return request_headers




