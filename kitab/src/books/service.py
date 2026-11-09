from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import bookCreateModel,BookUpdateModel
from sqlmodel import select,desc
from .models import Book

class Bookservice:
    
     async def get_all_books(self,session=AsyncSession):
        statement= select(Book).order_by(desc(Book.created_at))
        result=await session.exec(statement)
        return result.all()
     
     async def get_book(self,book_id:int,session=AsyncSession):
        statement= select(Book).where(Book.uid==book_id)
        res=await session.exec(statement)
        return res.first()
         
     async def create_book(self,book_data:bookCreateModel,session=AsyncSession):
         book_data_dict=book_data.model_dump()
         new_book=Book(**Book.dict)

         session.add(new_book)
         await session.commit()

         return new_book
     
async def update_book(self,book_id:str, update_book:BookUpdateModel,session=AsyncSession):
    book_to_update=self.get_book(book_id,session)
    update_data_dict=update_book.model_dump()

    for k,v in update_data_dict.items():
        setattr(book_to_update,k,v)

    await session.commit()
    return book_to_update 

async def delete_book(self,book_id:str,session=AsyncSession):
    book_to_delete=self.get_book(book_id,session)
    if book_to_delete is not None:
        await session.delete(book_to_delete)
        await session.commit()
    else:
        return None    