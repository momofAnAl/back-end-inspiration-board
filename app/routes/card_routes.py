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
    