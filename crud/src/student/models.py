from sqlmodel import SQLModel,Field,Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid


class Students(SQLModel,table=True):
   __tablename__="Student"
   uid:uuid.UUID=Field(
      sa_column=Column(pg.UUID,nullable=False, primary_key=True,default=uuid.uuid4)
   )
   name:str
   age:int
   health:int
   created_at:datetime=Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))
   updated_at:datetime=Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))


   def __repr__(self):
      return f"hello wold"


 