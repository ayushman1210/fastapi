from passlib .context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"], deprecrate="auto")

def get_password(password:str)->str:
    return pwd_context.hash(password)

def verify_password(plainpassword:str,hashedpassword:str)->bool:
    return pwd_context.verify(plainpassword,hashedpassword)