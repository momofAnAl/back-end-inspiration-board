from flask import Blueprint, abort, make_response, request
from app.models.board import Board
from app.db import db

bp = Blueprint("board_bp", __name__, url_prefix="/boards")

# @bp.get("")
# def get_all_saved_boards():
#     query = db.select(Board).order_by(Board.id)
#     boards = db.session.scalars(query)
    
#     response_body = []
#     return response_body
