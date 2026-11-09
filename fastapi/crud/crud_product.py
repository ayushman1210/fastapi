from typing import list

from sqlmodel import select

from sqlmodel.ext.asyncio.session import AsyncSession


from model.model import product
from schema import product_create
from sqlalchemy.orm import selectinload

async def create_product(product_data:product_create, session:AsyncSession)->product :
    db_product=product.model_validate(product_data)
    session.add(db_product)
    await session.commit()
    await session.refresh(db_product)
    return db_product


async def getallproducts(session:AsyncSession)->list[product]:
    statement=select(product)
    res=await session.exec(statement)
    return res.all()

async def get_product_by_id(id:int, session:AsyncSession)->product:
    statement=select(product).where(product.id==id)
    res=await session.exec(statement)
    return res.one_or_none()

