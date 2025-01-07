from app import create_app, db
from app.models.board import Board
from dotenv import load_dotenv

load_dotenv()

my_app = create_app()
with my_app.app_context():
    db.session.add(Board(title="Daily Motivation", owner="Anh"))
    db.session.add(Board(title="Coding Wisdom", owner="Jenny"))
    db.session.add(Board(title="Mindfulness Moments", owner="Brianna"))
    db.session.add(Board(title="Life Lessons", owner="Anna"))
   
    db.session.commit()