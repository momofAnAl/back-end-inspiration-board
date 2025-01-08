from flask import Flask
from flask_cors import CORS
from .db import db, migrate
from .models.board import Board
from .models.card import Card
from .routes.board_routes import bp as board_bp
from .routes.card_routes import bp as card_bp
import os


def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    # app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:postgres@localhost:5432/inspiration_board_development'

    if config:
        app.config.update(config)

    # Initialize app with SQLAlchemy db and Migrate
    db.init_app(app) 
    migrate.init_app(app, db)
    
    # Register Blueprints 
    app.register_blueprint(board_bp)
    app.register_blueprint(card_bp)


    CORS(app)
    return app
