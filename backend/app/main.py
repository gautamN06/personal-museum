from fastapi import FastAPI
from sqlalchemy import text 

from app.db import engine 

app = FastAPI()


@app.get("/")
def root():
    with engine.connect() as connection:
        result = connection.execute(text("Select 1"))

        return {
            "message" : "Welcome to my Personal Museum!",
            "database" : result.scalar(),
            }

