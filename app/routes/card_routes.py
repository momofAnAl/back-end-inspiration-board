from flask import Blueprint, abort, make_response, request, Response
from app.models.card import Card
from app.db import db
from app.routes.route_utilities import validate_model
import os

bp = Blueprint("card_bp", __name__, url_prefix="/cards")

@bp.get("")
def get_all_cards():
    query = db.select(Card)
    
    query= query.order_by(Card.id)
    cards = db.session.scalars(query)
    
    response_body = [card.to_dict() for card in cards]
    return response_body

@bp.get("/<card_id>")
def get_card(card_id):
    card = db.session.get(Card, card_id)
    
    response_body = {"card": card.to_dict()}
    return response_body

@bp.post("")
def create_card():
    request_body = request.get_json()
    if "message" not in request_body:
        response_body = {"details": "Invalid data"}
        return make_response(response_body, 400)
    
    message = response_body["message"]
    new_card = Card(message=message)
    
    db.session.add(new_card)
    db.session.commit()
    
    response_body = {"new_card": new_card.to_dict()}
    return response_body, 201
    

@bp.delete("/<card_id>")
def delete_card(card_id):
    card = db.session.get(Card, card_id)
  
    db.session.delete(card)
    db.session.commit()
    
    response_body = {"details": f'Card {card_id} "{card.message}" successfully deleted.'}
    
    return response_body

@bp.put("/<card_id>")
def update_card(card_id):
    card = db.session.get(Card, card_id)
    
    request_body = request.get_json()
    card.message = request_body["message"]
    
    db.session.commit()
    response_body = {"card": card.to_dict()}
    
    return make_response(response_body, 200)
    
    