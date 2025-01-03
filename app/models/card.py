from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from sqlalchemy import ForeignKey
from typing import Optional

class Card(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str]
    likes_count: Mapped[int] = mapped_column(default = 0, nullable=False)

    # This is a foreign key column that references the id column in the board table
    board_id: Mapped[Optional[int]] = mapped_column(ForeignKey("board.id")) 
    board: Mapped[Optional["Board"]] = relationship(back_populates="cards")

    # This is a method that returns a dictionary representation of the Card instance
    def to_dict(self):
        return {
            "id": self.id,
            "message": self.message,
            "likes_count": self.likes_count,
            "board_id": self.board_id,
        }

    # This is a class method that creates a new Card instance from a dictionary
    @classmethod 
    def from_dict(cls, card_data):
        new_card = cls(message=card_data["message"], likes_count=card_data["likes_count"], board_id=card_data["board_id"])
        return new_card
    
    