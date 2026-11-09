
from sqlmodel.ext.asyncio.session import AsyncSession
from .schema import student_create_model,student_update
from sqlmodel import select,desc
from .models import Students

class BookService:
    async def get_all_student(self,session:AsyncSession):
        statement=select(Students).order_by(desc(Students.created_at))
        result= await session.exec(statement=statement)
        return result.all()
    
    async def get_student(self,student_id:str,session:AsyncSession):
        statement=select((Students).where(Students.uid==student_id))
        result= await session.exec(statement=statement)
        return result.first()
    
    async def create_student(self,student_data:student_create_model,session:AsyncSession):
        student_data=student_data.model_dump()
        new_student=Students(
             **student_data
        )
        session.add(new_student)
        await session.commit()

        return new_student
         
    async def update_student(self,student_id:str,student_data:student_update,session:AsyncSession):
        student_to_update=self.get_student(student_id,session=session)

        update_data=student_data.model_dump()

        for k,v in update_data.items():
             setattr(student_to_update,k,v)

        await session.commit()

        return student_to_update

    async def delete_student(self,student_id:str,session:AsyncSession):
        book_to_delete=self.get_student(student_id,session)
        if book_to_delete is not None:
            await session.delete(book_to_delete)

            await session.commit()

            
