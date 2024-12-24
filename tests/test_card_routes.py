import pytest
from app import create_app, db
from app.models.board import Board
from app.models.card import Card

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_boards(app):
    board1 = Board(title="Board 1", owner="Owner 1")
    board2 = Board(title="Board 2", owner="Owner 2")
    db.session.add_all([board1, board2])
    db.session.commit()

@pytest.fixture
def two_cards(app, two_boards):
    card1 = Card(message="Card 1", board_id=1)
    card2 = Card(message="Card 2", board_id=2)
    db.session.add_all([card1, card2])
    db.session.commit()

def test_get_all_cards(client, two_cards):
    response = client.get("/cards")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2

def test_create_card(client, two_boards):
    response = client.post("/cards", json={"message": "New Card", "board_id": 1})
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body["message"] == "New Card"
    assert response_body["board_id"] == 1

def test_get_card(client, two_cards):
    response = client.get("/cards/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["message"] == "Card 1"
    assert response_body["board_id"] == 1

def test_update_card(client, two_cards):
    response = client.put("/cards/1", json={"message": "Updated Card"})
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["message"] == "Updated Card"

def test_delete_card(client, two_cards):
    response = client.delete("/cards/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert "successfully deleted" in response_body["details"]