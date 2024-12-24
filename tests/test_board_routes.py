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

def test_get_all_boards(client, two_boards):
    response = client.get("/boards")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2

def test_create_board(client):
    response = client.post("/boards", json={"title": "New Board", "owner": "New Owner"})
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body["title"] == "New Board"
    assert response_body["owner"] == "New Owner"

def test_get_board(client, two_boards):
    response = client.get("/boards/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["title"] == "Board 1"
    assert response_body["owner"] == "Owner 1"

def test_update_board(client, two_boards):
    response = client.put("/boards/1", json={"title": "Updated Board", "owner": "Updated Owner"})
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["board"]["title"] == "Updated Board"
    assert response_body["board"]["owner"] == "Updated Owner"

def test_delete_board(client, two_boards):
    response = client.delete("/boards/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert "successfully deleted" in response_body["details"]

def test_add_card_to_board(client, two_boards):
    response = client.post("/boards/1/cards", json={"message": "New Card"})
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body["message"] == "New Card"
    assert response_body["board_id"] == 1
    