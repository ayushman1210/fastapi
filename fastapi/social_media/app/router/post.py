
from .. import models,schema
from fastapi import status,FastAPI,Response,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from ..db import get_db
from .. import outh2
from .. import models
from typing import Optional
router=APIRouter(prefix='/posts',tags=["post"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=list[schema.Postresponse])
async def get_post(db:Session=Depends(get_db),current_user:int=Depends(outh2.get_user),Limit:int=3, skip:int=0,search:Optional[str]=""):
    post= db.query(models.Post).filter(models.Post.Content.contains(search)).limit(Limit).offset(skip).all()
    return post
 


@router.get('/{id}')
async def single_post(id:int,db:Session=Depends(get_db),user_id:int=Depends(outh2.get_user)):
    post_by_id=db.query(models.Post).filter(models.Post.id==user_id.id).first()
    return post_by_id 

@router.post('/',status_code=status.HTTP_201_CREATED, response_model=schema.Postresponse)
async def create_post(post:schema.Postmodel,db:Session=Depends(get_db),user:models.user=Depends(outh2.get_user)):
    new_post=models.Post(owner_id=user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.delete('/{id}')
async def delete_post(id:int, db:Session=Depends(get_db), user_id:models.user=Depends(outh2.get_user)):
    post=db.query(models.Post).filter(models.Post.id==id)
    if post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details=f"posts with this {id} not found")

    if post.first.owner_id!=user_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not authorize to do this action")
    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/{id}')
async def update_post(id:int, post:schema.Postmodel, db:Session=Depends(get_db),user_id:int=Depends(outh2.get_user)):
   post_query= db.query(models.Post).filter(models.Post.id==id)
   post=post_query.first()
   post_query.update(post.dict(),synchronize_session=False)

   db.commit()
   return post_query.first()
