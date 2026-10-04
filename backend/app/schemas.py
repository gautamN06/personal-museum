from pydantic import BaseModel 


class BookCreate(BaseModel):
    title: str 
    author: str 
    description: str | None = None 
    rating: int | None = None 
    personal_notes: str | None = None 

class BookResponse(BaseModel):
    id: int 
    title: str 
    author: str 
    description: str | None 
    rating: int | None 
    personal_notes: str | None 


class FigureCreate(BaseModel):
    name: str 
    religion: str | None = None 
    description: str | None = None 
    personal_notes: str | None = None 


class FigureResponse(BaseModel):
    id: int 
    name: str 
    religion: str | None 
    description: str  | None 
    personal_notes: str | None 