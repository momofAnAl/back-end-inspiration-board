import pytest
from app import create_app, db
from app.models.board import Board
from app.models.card import Card


#@pytest.mark.skip(reason="No way to test this feature yet")
def test_get_all_cards(client, two_saved_cards):
    response = client.get("/cards")
    response_body = response.get_json()

    print(response_body)

    assert response.status_code == 200
    assert len(response_body) == 2

#@pytest.mark.skip(reason="No way to test this feature yet")
def test_create_card_to_board(client, two_saved_boards):
    board_id = 1
    response = client.post(f"/{board_id}/cards", json={"message": "New Card"})
    response_body = response.get_json()

    assert response.status_code == 201
    assert "message" in response_body
    assert response_body["message"] == "New Card"
    assert response_body["board_id"] == board_id

@pytest.mark.skip(reason="No way to test this feature yet")
def test_get_card(client, two_saved_cards):
    response = client.get("/cards/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["message"] == "Card 1"
    assert response_body["board_id"] == 1

@pytest.mark.skip(reason="No way to test this feature yet")
def test_update_card(client, two_saved_cards):
    response = client.put("/cards/1", json={"message": "Updated Card"})
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["message"] == "Updated Card"

@pytest.mark.skip(reason="No way to test this feature yet")
def test_delete_card(client, two_saved_cards):
    response = client.delete("/cards/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert "successfully deleted" in response_body["details"]