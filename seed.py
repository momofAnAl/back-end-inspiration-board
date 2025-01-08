from app import create_app, db
from app.models.card import Card
from dotenv import load_dotenv

load_dotenv()

my_app = create_app()
with my_app.app_context():
    db.session.add(Card(board_id=1,message="Dream big, work hard, stay focused, and surround yourself with good people.")),
    db.session.add(Card(board_id=1,message="Success is not final, failure is not fatal: it is the courage to continue that counts.")),
    db.session.add(Card(board_id=1,message="When in doubt, take a break. A fresh mind sees fresh solutions.")),
    db.session.add(Card(board_id=1,message="You are capable of amazing things. Keep going!")),
    db.session.add(Card(board_id=1,message="Great things are not done by impulse, but by a series of small things brought together.")),
    db.session.add(Card(board_id=1,message="There’s always a way to improve and learn something new.")),
    db.session.add(Card(board_id=1,message="Keep your face always toward the sunshine—and shadows will fall behind you.")),
    db.session.add(Card(board_id=2,message="One bug at a time, one feature at a time. You're doing great!")),
    db.session.add(Card(board_id=2,message="The best way to predict the future is to create it.")),
    db.session.add(Card(board_id=2,message="Start where you are. Use what you have. Do what you can.")),
    db.session.add(Card(board_id=2,message="You are stronger than you think, and braver than you know.")),
    db.session.add(Card(board_id=2,message="Every day is a new beginning. Take a deep breath and start again.")),
    db.session.add(Card(board_id=2,message="Don't be afraid to fail. Be afraid not to try.")),
    db.session.add(Card(board_id=2,message="Your past does not define your future. Every day is a new chance.")),
    db.session.add(Card(board_id=3,message="Happiness is not something ready-made. It comes from your own actions.")),
    db.session.add(Card(board_id=3,message="Mistakes are proof that you are trying.")),
    db.session.add(Card(board_id=3,message="When you feel like quitting, remember why you started.")),
    db.session.add(Card(board_id=3,message="Sometimes, the smallest step in the right direction ends up being the biggest step of your life.")),
    db.session.add(Card(board_id=3,message="Take pride in how far you’ve come and have faith in how far you can go.")),
    db.session.add(Card(board_id=3,message="Your value doesn’t decrease based on someone’s inability to see your worth.")),
    db.session.add(Card(board_id=3,message="You can. End of story.")),
    db.session.add(Card(board_id=4,message="If you're tired, rest. Don't quit.")),
    db.session.add(Card(board_id=4,message="You deserve the love you so freely give to others.")),
    db.session.add(Card(board_id=4,message="Progress, not perfection. Every step counts.")),
    db.session.add(Card(board_id=4,message="Be kind to yourself. You’re doing the best you can.")),
    db.session.add(Card(board_id=4,message="The sun will rise, and you will try again.")),
    db.session.add(Card(board_id=4,message="You don’t have to have it all figured out to move forward.")),
    
    db.session.commit()