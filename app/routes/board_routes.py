from flask import Blueprint, abort, make_response, request
from app.models.board import Board
from app.models.card import Card
from app.db import db
from app.routes.route_utilities import validate_model

bp = Blueprint("board_bp", __name__, url_prefix="/boards")

@bp.get("")
def get_all_saved_boards():
    query = db.select(Board).order_by(Board.id)
    boards = db.session.scalars(query)
    
    response_body = [board.to_dict() for board in boards]
    return response_body

@bp.get("/<board_id>")
def get_board(board_id):
    board = db.session.get(Board, board_id)
    db.session.add(board)
    db.session.commit()

    all_cards = [card.to_dict() for card in board.cards]
    response_body = {"board": board.to_dict(), "cards": all_cards}
    
    return response_body

@bp.post("")
def create_board():
    request_body = request.get_json()
    if "title" not in request_body and "owner" not in request_body:
        response_body = {"details": "Invalid data"}
        return make_response(response_body, 400)

    title = request_body["title"]
    owner = request_body["owner"]
    new_board = Board(title=title, owner=owner)
    db.session.add(new_board)
    db.session.commit()
    
    response_body = new_board.to_dict()
    
    return response_body,201

@bp.delete("/<board_id>")
def delete_board(board_id):
    board = validate_model(Board, board_id)
    
    response_body = {"details": f'Board {board_id} "{board.title}" of "{board.owner}" successfully deleted.'}
    return make_response(response_body, 200)

@bp.put("/<board_id>")
def update_board(board_id):
    board = validate_model(Board, board_id)

    request_body = request.get_json()
    board.title = request_body.get("title", board.title)
    board.owner = request_body.get("owner", board.owner)
    
    db.session.commit()
    
    response_body = {"board": board.to_dict()}
    return make_response(response_body, 200)

@bp.post("/<board_id>/cards")
def create_card_to_board(board_id):
    board = validate_model(Board, board_id)
    
    request_body = request.get_json()
    message = request_body["message"]
    if "message" not in request_body:
        request_body = {"details": "Card message is required"}
        return make_response(response_body, 400)
    if len(message) > 40:
        return make_response(({"details": "Card message must be 40 characters or less"}), 400)
    

    
    new_card = Card(message=message, board=board)
    db.session.add(new_card)
    db.session.commit()
    
    response_body = new_card.to_dict()
    
    return response_body, 201

@bp.get("/<board_id>/cards")
def get_cards_for_board(board_id):
    board = validate_model(Board, board_id)
    cards = db.session.query(Card).filter_by(board_id=board.id).order_by(Card.id).all()

    response_body = dict(
        id=board.id,
        title=board.title,
        owner=board.owner,
        cards=[card.to_dict() for card in cards]
    )
    return response_body    