from app.models import Manufacturer, Ship, Type, db
from app import app
from dotenv import load_dotenv
load_dotenv()


with app.app_context():
    db.drop_all()
    db.create_all()

    man1 = Manufacturer(name='Man1')
    man2 = Manufacturer(name='Man2')

    type1 = Type(name='Military')

    ship1 = Ship(
        name='DeathStar',
        manufacturer_id=1,
        type_id=1,
        size=500,
        designer='Darth Vader',
        crew_cap=8000,
        travel_range=3,
        ftl=True,
        used=True,
        model_link='place_holder',
        description='Big black circle, causes destruction',
        stock=1,
        price=1000000000
    )

    ship2 = Ship(
        name='BigShip',
        manufacturer_id=2,
        type_id=1,
        size=5000,
        designer='Ian',
        crew_cap=50000,
        travel_range=3,
        ftl=False,
        used=False,
        model_link='place_holder',
        description='Pretty big ship',
        stock=1,
        price=300000
    )

    db.session.add(man1)
    db.session.add(man2)
    db.session.add(type1)
    db.session.add(ship1)
    db.session.add(ship2)

    db.session.commit()
