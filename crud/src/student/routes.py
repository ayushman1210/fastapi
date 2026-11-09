from fastapi import FastAPI,Header,status,APIRouter
# from typing import Optional
from typing import List
from src.student.student_data import student
from src.student.schema import student_update,Students
from fastapi.exceptions import HTTPException

student_router=APIRouter()
@student_router.get('/',response_model=List[Students])
async def get_student():
    return student


@student_router.post('/create',status_code=status.HTTP_201_CREATED)
async def create_student(student_data:Students)->dict:
   new_student=student_data.model_dump() 
   student.append(new_student)
   return new_student

    

@student_router.get('/{student_id}')
async def get_student_detail(student_id:int):
   for children in student:
      if(children['id']==student_id):
         return children
   raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="student not found"
      ) 

@student_router.patch('/{student_id}')
async def update_student_detail(student_id:int,update_data:student_update):
   for children in student:
      if(children["id"]==student_id):
         children["name"]=update_data.name
         children["age"]=update_data.age
         return children

   raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="student is not found")   
   

@student_router.delete('/{student_id}')
async def delete_student_detail(student_id:int)->dict:
   for child in student:
      if (child["id"]==student_id):
         student.remove(child)
         return{}
   raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="student is not found")      

    
    