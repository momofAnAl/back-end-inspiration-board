from sqlalchemy.orm import Mapped, mapped_column, relationship 
from ..db import db
# from .card import Card


class Board(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    owner: Mapped[str]

    cards: Mapped[list["Card"]] = relationship(back_populates="board")
