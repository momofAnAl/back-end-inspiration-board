import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
import os
from app.models.board import Board
from app.models.card import Card

load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_boards(app):
    # Arrange
    board1 = Board(title="Board 1",
                            owner="Owner 1")
    
    board2 = Board(title="Board 2",
                            owner="Owner 2")

    db.session.add_all([board1, board2])
    db.session.commit()

    return [board1, board2]

@pytest.fixture
def two_saved_cards(app, two_saved_boards):

    board1, board2 = two_saved_boards  

    card1 = Card(board_id=1, 
                    message="You are enough, just as you are.",)
    
    card2 = Card(board_id=1, 
                    message="If you're tired, rest. Don't quit.")

    db.session.add_all([card1, card2])
    db.session.commit()

    return [card1, card2]
