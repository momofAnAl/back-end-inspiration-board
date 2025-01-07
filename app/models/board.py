from sqlalchemy.orm import Mapped, mapped_column, relationship 
from ..db import db
from app.models.card import Card


# Import the Card model
class Board(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    owner: Mapped[str]
    cards: Mapped[list["Card"]] = relationship(back_populates="board")

    # This is a method that returns a dictionary representation of the Board instance
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "owner": self.owner,
        }
    
    # This is a class method that creates a new Board instance from a dictionary
    @classmethod 
    def from_dict(cls, board_data):
        new_board = cls(title=board_data["title"], owner=board_data["owner"])
        return new_board
