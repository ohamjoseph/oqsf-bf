# from datetime import datetime
#
# from sqlalchemy import create_engine, Column, Integer, DateTime, event
# from sqlalchemy.ext.declarative import as_declarative, declared_attr
# from sqlalchemy.orm import sessionmaker
#
# SQLALCHEMY_DATABASE_URL = "sqlite:///./reclamations.db"
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# @as_declarative()
# class Base:
#     id = Column(Integer, primary_key=True, index=True)
#     __name__: str
#
#     @declared_attr
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower()
#
#     createDate = Column(DateTime, default=datetime.utcnow, nullable=True)
#     updateDate = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True)
#
#
# @event.listens_for(Base, "before_insert", propagate=True)
# def set_create_date(mapper, connection, target):
#     target.createDate = datetime.utcnow()
#     target.updateDate = datetime.utcnow()
#
# @event.listens_for(Base, "before_update", propagate=True)
# def set_update_date(mapper, connection, target):
#     target.updateDate = datetime.utcnow()
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, DateTime, TIMESTAMP
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base, as_declarative,  declared_attr
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

#DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_LINK = os.getenv("DATABASE_LINK")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_URL = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_LINK}:{DATABASE_PORT}/{DATABASE_NAME}'

# Créer l'engine avec psycopg2-binary
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, index=True)
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    createDate = Column(TIMESTAMP, default=datetime.utcnow, nullable=True)
    updateDate = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

