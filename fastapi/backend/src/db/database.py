from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.orm import declarative_base, sessionmaker


sql_alchemy_database="postgresql+async_driver://postgres:Aas%402010@localhost/Backend"

engine = create_engine(
    make_url(sql_alchemy_database).set(drivername="postgresql+psycopg"),
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

def get_db():
    with SessionLocal() as db:
        yield db 