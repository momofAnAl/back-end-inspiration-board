import pytest
from app import create_app, db
from app.models.board import Board

#@pytest.mark.skip(reason="No way to test this feature yet")
def test_get_all_boards(client, two_saved_boards):
    response = client.get("/boards")
    response_body = response.get_json()  

    assert response.status_code == 200  
    assert len(response_body) == 2  



#@pytest.mark.skip(reason="No way to test this feature yet")
def test_create_board(client):
    response = client.post("/boards", json={"title": "New Board", "owner": "New Owner"})
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body["title"] == "New Board"
    assert response_body["owner"] == "New Owner"


#@pytest.mark.skip(reason="No way to test this feature yet")
def test_get_board_by_id(client, two_saved_boards):
    response = client.get("/boards/1")
    response_body = response.get_json()

    board = response_body.get("board", {})

    assert response.status_code == 200
    assert board.get("title") == "Board 1"
    assert board.get("owner") == "Owner 1"


#@pytest.mark.skip(reason="No way to test this feature yet")
def test_update_board(client, two_saved_boards):
    response = client.put("/boards/1", json={"title": "Updated Board", "owner": "Updated Owner"})
    response_body = response.get_json()



    assert response.status_code == 200
    assert response_body["board"]["title"] == "Updated Board"
    assert response_body["board"]["owner"] == "Updated Owner"

#@pytest.mark.skip(reason="No way to test this feature yet")
def test_delete_board(client, two_saved_boards):
    response = client.delete("/boards/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert "successfully deleted" in response_body["details"]

#@pytest.mark.skip(reason="No way to test this feature yet")
def test_add_card_to_board(client, two_saved_boards):
    response = client.post("/boards/1/cards", json={"message": "New Card"})
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body["message"] == "New Card"
    assert response_body["board_id"] == 1


    