from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app.db import Base, engine
from app.models import Book


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

        return {
            "message": "Welcome to my Personal Museum!",
            "database": result.scalar(),
        }
    