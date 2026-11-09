from typing import list 
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession 
from core.db import get_session
from crud import crud_product
from schema import ProductPublic,product_create

router=APIRouter()

@router.post("/create_post",status_code=status.HTTP_201_CREATED)
async def create_new_product(product_data:product_create,session:AsyncSession=Depends(get_session)):
    new_product=await crud_product.create_product(product_data=product_data,session=session)

@router.get("/",response_model=list[ProductPublic])    
async def get_all_product(session:AsyncSession=Depends(get_session)):
    product=await crud_product.getallproducts(session=session)
    return product

@router.get("/{id}",response_model=ProductPublic)
async def get_product_detail(id:int,session:AsyncSession=Depends(get_session)):
    product=await  crud_product.get_product_by_id(id==id, session=session)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details="product with id not found")
    return product