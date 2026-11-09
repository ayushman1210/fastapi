


from .. import models,schema,utils
from fastapi import status,FastAPI,Response,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from ..db import get_db


router=APIRouter(prefix="/user", tags=["users"])

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schema.user_response)
async def hell(users:schema.user_created,db:Session=Depends(get_db)):
    hashed_password=utils.hashed_password(users.password)
    users.password=hashed_password
    new_user=models.user(**users.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schema.user_response)
async def get_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.user).filter(models.user.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details=f"User with id {id} does not exist")

    return user 