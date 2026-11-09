from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from psycopg2.extras import RealDictCursor
import psycopg2
import time
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:Aas%402010@localhost/Hello"


engine=create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
try:
    conn=psycopg2.connect(host='localhost',database='Hello',user='postgres',password='Aas@2010',cursor_factory=RealDictCursor)
    cursor=conn.cursor()
    print('db is connected')
except Exception as error:
    print("connecting to databases is in error")
    print("error is ",error)
    time.sleep(2)    
