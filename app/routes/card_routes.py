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
    # card = db.session.get(Card, card_id)
    # response_body = {"card": card.to_dict()}
    # return response_body
    
    card = validate_model(Card, card_id)
    return card.to_dict(), 200

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
    response_body = card.to_dict()
    
    return make_response(response_body, 200)
    
@bp.patch("/<card_id>/like")
def like_card(card_id):
    card = db.session.get(Card, card_id)  
    
    if card.likes_count:
        card.likes_count += 1
    else:
        card.likes_count = 1

    # if card.likes_count is None:
    #     card.likes_count = 0
    # card.likes_count += 1
    
    db.session.commit()
    
    response_body = card.to_dict()
    return make_response(response_body, 200)
     