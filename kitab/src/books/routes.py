from src.books.service import Bookservice
from src.books.models import Book
from fastapi import APIRouter,status,Depends,HTTPException
from src.books.schemas import Book,bookCreateModel
from sqlmodel.ext.asyncio.session import AsyncSession 
from src.db.main import get_session
from datetime import datetime
book_router=APIRouter()
book_service=Bookservice()

@book_router.get("/",response_model=list[Book])
async def get_all_books(session:AsyncSession=Depends(get_session)):
    books=Bookservice.get_all_books(session)
    return books

@book_router.post("/create_book",status_code=status.HTTP_201_CREATED)
async def create_book(book_data:Book,session:AsyncSession=Depends(get_session))->dict:
    new_book=Bookservice.create_book(book_data,session)
    new_book.published_at=datetime.strptime(new_book['published_at'],"%Y-%m-%d")
    return new_book


@book_router.get("/{book_id}")
async def update_book(book_id:int,session:AsyncSession=Depends(get_session)):
    book=Bookservice.get_book(book_id,session)
    if book:
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book not found")
        