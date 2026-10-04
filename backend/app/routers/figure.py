from fastapi import APIRouter 
from sqlalchemy.orm import Session 

from app.db import engine 
from app.models import Figure 
from app.schemas import FigureCreate, FigureResponse 

router = APIRouter(prefix="/figures", tags=["Figures"])


@router.post("/", response_model=FigureResponse)
def create_book(figure: FigureCreate):
    with Session(engine) as session: 
        new_figure = Figure(
            name = figure.name, 
            religion = figure.religion, 
            description = figure.description,
            personal_notes = figure.personal_notes,
        )

        session.add(new_figure)
        session.commit()
        session.refresh(new_figure)

        return new_figure  
