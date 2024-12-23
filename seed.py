from app import create_app, db
from app.models.card import Card

my_app = create_app()
with my_app.app_context():
    db.session.add((message: "" )),