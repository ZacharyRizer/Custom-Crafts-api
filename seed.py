from app.models import Manufacturer, Ship, Category, db
from app import app
from dotenv import load_dotenv
load_dotenv()

# size 1 = 100, 100-500, 500-1000, 1000-5000, 5000+
# price = 10000, 10000-100000, 100000-500000, 500000-1000000, 1000000+
# range = 25, 25-100, 100-1000, 1000-10000, 10000+
# crew_cap = 10, 10-100, 100-500, 500-1000, 1000+

with app.app_context():
    db.drop_all()
    db.create_all()

    man1 = Manufacturer(name='Imperial Galactic Government')
    man2 = Manufacturer(name='Spacing Guild')
    man3 = Manufacturer(name='Corellian Engineering Corporation')
    man4 = Manufacturer(name='Cybertronian Technologies')
    man5 = Manufacturer(name='Weyland-Yutani Corporation')

    cat1 = Category(name='Military')
    cat2 = Category(name='Transport')
    cat3 = Category(name='Cargo')
    cat4 = Category(name='Performance')
    cat5 = Category(name='Luxury')

    ship1 = Ship(
        name='Frontier',
        manufacturer_id=1,
        category_id=1,
        size=8473,
        designer='T\'Maha',
        crew_cap=2500,
        travel_range=15600,
        ftl=True,
        used=False,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=47000000
    )
    ship2 = Ship(
        name='SS Dreadnought',
        manufacturer_id=1,
        category_id=1,
        size=4788,
        designer='Glama V\'Leeni',
        crew_cap=1000,
        travel_range=9500,
        ftl=False,
        used=True,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=8500000
    )
    ship3 = Ship(
        name='Despot',
        manufacturer_id=1,
        category_id=1,
        size=8993,
        designer='Kr\'Andull',
        crew_cap=500,
        travel_range=8700,
        ftl=True,
        used=False,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=15000000
    )
    ship4 = Ship(
        name='Star Talon',
        manufacturer_id=2,
        category_id=2,
        size=340,
        designer='Aren Bellee',
        crew_cap=350,
        travel_range=850,
        ftl=False,
        used=True,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=870000
    )
    ship5 = Ship(
        name='Proton',
        manufacturer_id=2,
        category_id=2,
        size=945,
        designer='Zach Rizer',
        crew_cap=10,
        travel_range=13000,
        ftl=True,
        used=False,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=954000
    )
    ship6 = Ship(
        name='Trenxal',
        manufacturer_id=2,
        category_id=2,
        size=86,
        designer='Vlegi Moveloi',
        crew_cap=50,
        travel_range=359,
        ftl=False,
        used=True,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=657000
    )
    ship7 = Ship(
        name='The Rubber Ducky',
        manufacturer_id=3,
        category_id=3,
        size=10,
        designer='Ian Magenta',
        crew_cap=2,
        travel_range=25,
        ftl=True,
        used=False,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=3500
    )
    ship8 = Ship(
        name='The Æthelwulf',
        manufacturer_id=3,
        category_id=3,
        size=1212,
        designer='Take Mayuma',
        crew_cap=50,
        travel_range=3,
        ftl=False,
        used=True,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=670000
    )
    ship9 = Ship(
        name='Poseidon',
        manufacturer_id=3,
        category_id=3,
        size=7564,
        designer='Sui Gwu-Pao',
        crew_cap=1200,
        travel_range=5800,
        ftl=True,
        used=False,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=890000
    )
    ship10 = Ship(
        name='Apollo',
        manufacturer_id=4,
        category_id=4,
        size=765,
        designer='William Schraeder',
        crew_cap=300,
        travel_range=3500,
        ftl=False,
        used=True,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=435000
    )
    ship11 = Ship(
        name='Oberon Nova',
        manufacturer_id=4,
        category_id=4,
        size=276,
        designer='Valdis Simril',
        crew_cap=100,
        travel_range=4500,
        ftl=True,
        used=False,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=87000
    )
    ship12 = Ship(
        name='ISV Rimward Gold',
        manufacturer_id=4,
        category_id=4,
        size=764,
        designer='Guinevere Watrous',
        crew_cap=250,
        travel_range=900,
        ftl=False,
        used=True,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=96000
    )
    ship13 = Ship(
        name='Rimward Perseus',
        manufacturer_id=5,
        category_id=5,
        size=476,
        designer='Derrik Alder',
        crew_cap=100,
        travel_range=5700,
        ftl=True,
        used=False,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=9999
    )
    ship14 = Ship(
        name='Tycho',
        manufacturer_id=5,
        category_id=5,
        size=156,
        designer='Maddox Volante',
        crew_cap=50,
        travel_range=7500,
        ftl=False,
        used=True,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=65000
    )
    ship15 = Ship(
        name='The Leviathan',
        manufacturer_id=5,
        category_id=5,
        size=3745,
        designer='Abdullah Wafy',
        crew_cap=1000,
        travel_range=12000,
        ftl=True,
        used=False,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=956000
    )

    db.session.add(man1)
    db.session.add(man2)
    db.session.add(man3)
    db.session.add(man4)
    db.session.add(man5)

    db.session.add(cat1)
    db.session.add(cat2)
    db.session.add(cat3)
    db.session.add(cat4)
    db.session.add(cat5)

    db.session.add(ship1)
    db.session.add(ship2)
    db.session.add(ship3)
    db.session.add(ship4)
    db.session.add(ship5)
    db.session.add(ship6)
    db.session.add(ship7)
    db.session.add(ship8)
    db.session.add(ship9)
    db.session.add(ship10)
    db.session.add(ship11)
    db.session.add(ship12)
    db.session.add(ship13)
    db.session.add(ship14)
    db.session.add(ship15)

    db.session.commit()
