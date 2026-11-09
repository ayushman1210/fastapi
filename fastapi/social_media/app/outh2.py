from jose import JWTError,jwt
from datetime import datetime,timedelta
from fastapi import Depends,status,HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from . import schema,db,models


outh2_schema=OAuth2PasswordBearer(tokenUrl='login')
SECRET_KEY="JWT_SECRET"
ALGORITHM="HS256"
Acess_token_expire_minute=30


def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=Acess_token_expire_minute)
    to_encode.update({"exp":expire})

    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt



def verify_access_token(token:str,credential_exception):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id:str=payload.get("user_id")

        if id is None:
            raise credential_exception
        token_data=schema.tokendata(id=str(id))
    except JWTError as e:
        print(e)
        raise credential_exception   
    return token_data 

def get_user(token:str=Depends(outh2_schema),db:Session=Depends(db.get_db)):
    credential_exception=HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"could not validate credential",headers={"WWW-Authenticate":"Bearer"})
    token=verify_access_token(token,credential_exception)
    new_user=db.query(models.user).filter(models.user.id==token.id).first()
    return new_user