from sqlalchemy.orm import Mapped, mapped_column, relationship 
from ..db import db

class Card(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    string: Mapped[str]
    likes_count: Mapped[int]