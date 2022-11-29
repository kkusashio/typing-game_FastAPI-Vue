from sqlalchemy.orm import sessionmaker, declarative_base, Session, scoped_session
from sqlalchemy import create_engine

DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"

engine = create_engine(DB_URL, echo=True)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    # with session() as session:
    #     yield session
    db = session()
    try:
        yield db
    finally:
        db.close()
