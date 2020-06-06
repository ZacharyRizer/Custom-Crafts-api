from app.models import Manufacturer, db
from app import app
from dotenv import load_dotenv
load_dotenv()


with app.app_context():
    db.drop_all()
    db.create_all()

    man1 = Manufacturer(name='Man1')
    man2 = Manufacturer(name='Man2')

    db.session.add(man1)
    db.session.add(man2)
    db.session.commit()
