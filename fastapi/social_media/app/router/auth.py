from fastapi import status,APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import db,schema,models,utils,outh2
router=APIRouter(tags=['AUTHENTICATION'])


@router.post('/login',response_model=schema.token)
async def login_user(user_credential:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(db.get_db)):
    user=db.query(models.user).filter(models.user.email==user_credential.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid credentials")

    if not utils.verify(user_credential.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"invalid credentials password does not match ")


    access_token=outh2.create_access_token(data={"user_id":user.id}) 
    return {"acess_token":access_token, "token_type":"bearer"}