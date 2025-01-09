from flask import Blueprint, abort, make_response, request, Response
from app.models.card import Card
from app.db import db
from app.routes.route_utilities import validate_model
import os

bp = Blueprint("card_bp", __name__, url_prefix="/cards")

@bp.delete("/<card_id>")
def delete_card(card_id):
    card = db.session.get(Card, card_id)
  
    db.session.delete(card)
    db.session.commit()
    
    response_body = {"details": f'Card {card_id} "{card.message}" successfully deleted.'}
    
    return response_body

    
@bp.patch("/<card_id>/like")
def like_card(card_id):
    card = db.session.get(Card, card_id)  
    
    if card.likes_count:
        card.likes_count += 1
    else:
        card.likes_count = 1
    
    db.session.commit()
    
    response_body = card.to_dict()
    return make_response(response_body, 200)
     