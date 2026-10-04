from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    author: Mapped[str] = mapped_column(String(200))
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    rating: Mapped[int | None] = mapped_column(nullable=True)
    personal_notes: Mapped[str | None] = mapped_column(Text, nullable=True)

class Figure(Base):
    __tablename__ = "figure"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    religion: Mapped[str | None] = mapped_column(String(200))
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    personal_notes: Mapped[str | None] = mapped_column(Text, nullable=True)


