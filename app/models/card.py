from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from sqlalchemy import ForeignKey
# from .board import Board
from typing import Optional

class Card(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str]
    likes_count: Mapped[int] = mapped_column(nullable=True)

    board_id: Mapped[Optional[int]] = mapped_column(ForeignKey("board.id")) 
    board: Mapped[Optional["Board"]] = relationship(back_populates="cards")