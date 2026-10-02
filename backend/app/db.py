from sqlalchemy import create_engine 
from sqlalchemy.orm import DeclarativeBase


DATABASE_URL = "postgresql+psycopg://postgres:KedarNath1.@localhost:5432/personal_museum"

engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass 

