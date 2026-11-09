from .db import Base
from sqlalchemy import Column,Integer,String,Boolean,TIMESTAMP,ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
class Post(Base):
    __tablename__="posts"
    id=Column(Integer,primary_key=True,nullable=False)
    Title=Column(String,nullable=False)
    Content=Column(String,nullable=False)
    published=Column(Boolean,nullable=False,server_default='TRUE')
    created_at=Column(TIMESTAMP, nullable=False,server_default=text('now()')) 
    owner_id=Column(Integer, ForeignKey("user.id",ondelete="CASCADE"),nullable=False)
    owner=relationship("user")

class user(Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True,nullable=False)
    email=Column(String,nullable=False, unique=True)
    password=Column(String, nullable=False)    
    created_at=Column(TIMESTAMP, nullable=False,server_default=text('now()'))  
    
   




