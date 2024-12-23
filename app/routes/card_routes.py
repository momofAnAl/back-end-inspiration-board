from flask import Blueprint, abort, make_response, request, Response
from app.models.card import Card
from app.db import db
import os
import requests

bp = Blueprint("card_bp", __name__, url_prefix="/cards")

@bp.get("")
def get_all_cards():
    query = db.select(Card)
    
    query= query.order.by(Card.id)
    cards = db.session.scalar
    
    response_body = []
    return response_body
    