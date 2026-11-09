from pydantic import BaseModel



class Students(BaseModel):
   id:int
   name:str
   age:int
   health:int


class student_update(BaseModel):
   name:str
   age:int  

class student_create_model(BaseModel):
      name:str
      age:int
   