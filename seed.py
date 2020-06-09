from app.models import Manufacturer, Ship, Category, db
from app import app
from dotenv import load_dotenv
load_dotenv()


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
        size=10000,
        designer='T\'Maha',
        crew_cap=1000,
        travel_range=5,
        ftl=True,
        used=False,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=1000000000
    )
    ship2 = Ship(
        name='SS Dreadnought',
        manufacturer_id=1,
        category_id=1,
        size=5000,
        designer='Glama V\'Leeni',
        crew_cap=1000,
        travel_range=4,
        ftl=False,
        used=True,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=1000000000
    )
    ship3 = Ship(
        name='Despot',
        manufacturer_id=1,
        category_id=1,
        size=15000,
        designer='Kr\'Andull',
        crew_cap=500,
        travel_range=3,
        ftl=True,
        used=False,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=1000000000
    )
    ship4 = Ship(
        name='Star Talon',
        manufacturer_id=2,
        category_id=2,
        size=500,
        designer='Aren Bellee',
        crew_cap=1000,
        travel_range=2,
        ftl=False,
        used=True,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=1000000
    )
    ship5 = Ship(
        name='Proton',
        manufacturer_id=2,
        category_id=2,
        size=1000,
        designer='Zach Rizer',
        crew_cap=10,
        travel_range=1,
        ftl=True,
        used=False,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=50000000
    )
    ship6 = Ship(
        name='Trenxal',
        manufacturer_id=2,
        category_id=2,
        size=50000,
        designer='Vlegi Moveloi',
        crew_cap=500,
        travel_range=5,
        ftl=False,
        used=True,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=800000
    )
    ship7 = Ship(
        name='The Rubber Ducky',
        manufacturer_id=3,
        category_id=3,
        size=2000,
        designer='Ian Magenta',
        crew_cap=2,
        travel_range=4,
        ftl=True,
        used=False,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=100000
    )
    ship8 = Ship(
        name='The Æthelwulf',
        manufacturer_id=3,
        category_id=3,
        size=20000,
        designer='Take Mayuma',
        crew_cap=50,
        travel_range=3,
        ftl=False,
        used=True,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=1000000000
    )
    ship9 = Ship(
        name='Poseidon',
        manufacturer_id=3,
        category_id=3,
        size=10000,
        designer='Sui Gwu-Pao',
        crew_cap=3000,
        travel_range=2,
        ftl=True,
        used=False,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=800000000
    )
    ship10 = Ship(
        name='Apollo',
        manufacturer_id=4,
        category_id=4,
        size=5000,
        designer='William Schraeder',
        crew_cap=300,
        travel_range=1,
        ftl=False,
        used=True,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=20000000
    )
    ship11 = Ship(
        name='Oberon Nova',
        manufacturer_id=4,
        category_id=4,
        size=20000,
        designer='Valdis Simril',
        crew_cap=100,
        travel_range=5,
        ftl=True,
        used=False,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=500000
    )
    ship12 = Ship(
        name='ISV Rimward Gold',
        manufacturer_id=4,
        category_id=4,
        size=1000,
        designer='Guinevere Watrous',
        crew_cap=500,
        travel_range=4,
        ftl=False,
        used=True,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=5000000
    )
    ship13 = Ship(
        name='Rimward Perseus',
        manufacturer_id=5,
        category_id=5,
        size=5000,
        designer='Derrik Alder',
        crew_cap=1000,
        travel_range=3,
        ftl=True,
        used=False,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=1000000000
    )
    ship14 = Ship(
        name='Tycho',
        manufacturer_id=5,
        category_id=5,
        size=10000,
        designer='Maddox Volante',
        crew_cap=100,
        travel_range=2,
        ftl=False,
        used=True,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=5000000
    )
    ship15 = Ship(
        name='The Leviathan',
        manufacturer_id=5,
        category_id=5,
        size=10000,
        designer='Abdullah Wafy',
        crew_cap=1000,
        travel_range=1,
        ftl=True,
        used=False,
        model_link='/spaceships/test_ship.glb',
        description='Big black circle, causes destruction',
        stock=3,
        price=1000000000
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
