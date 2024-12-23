from flask import Blueprint, request
# from route_utilities import validate_model
from app.models.board import Board
from app.models.card import Card
from app.db import db


board_bp = Blueprint("board_bp", __name__, url_prefix="/boards")

