from app import create_app, db
from app.models.card import Card

my_app = create_app()
with my_app.app_context():
    db.session.add(Card(message="Believe in yourself and all that you are.")),
    db.session.add(Card(message="Every great developer you know started as a beginner.")),
    db.session.add(Card(message="Code is like humor. When you have to explain it, it’s bad.")),
    db.session.add(Card(message="Strive for progress, not perfection.")),
    db.session.add(Card(message="Your only limit is your mind.")),
    db.session.add(Card(message="Debugging is like being a detective in a crime movie where you're also the murderer.")),
    db.session.add(Card(message="Dream big, work hard, stay focused, and surround yourself with good people.")),
    db.session.add(Card(message="Success is not final, failure is not fatal: it is the courage to continue that counts.")),
    db.session.add(Card(message="When in doubt, take a break. A fresh mind sees fresh solutions.")),
    db.session.add(Card(message="You are capable of amazing things. Keep going!")),
    db.session.add(Card(message="Great things are not done by impulse, but by a series of small things brought together.")),
    db.session.add(Card(message="There’s always a way to improve and learn something new.")),
    db.session.add(Card(message="Keep your face always toward the sunshine—and shadows will fall behind you.")),
    db.session.add(Card(message="One bug at a time, one feature at a time. You're doing great!")),
    db.session.add(Card(message="The best way to predict the future is to create it.")),
    db.session.add(Card(message="Start where you are. Use what you have. Do what you can.")),

    db.session.commit()