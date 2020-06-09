from app.models import Manufacturer, Ship, Category, db
from app import app
from dotenv import load_dotenv
load_dotenv()

# size 1 = 100, 100-500, 500-1000, 1000-5000, 5000+
# price = 10000, 10000-100000, 100000-5000000, 500000-1000000, 1000000+
# range = 1, 1-100, 100-1000, 1000-10000, 10000+
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
        display_size=8473,
        size_id=5,
        designer='T\'Maha',
        crew_id=5,
        range_id=5,
        ftl=True,
        used=False,
        model_link='place_holder',
        description='Big black circle, causes destruction',
        stock=3,
        display_price=47000000,
        price_id=5
    )
    ship2 = Ship(
        name='SS Dreadnought',
        manufacturer_id=1,
        category_id=1,
        display_size=4788,
        size_id=4,
        designer='Glama V\'Leeni',
        crew_id=4,
        range_id=4,
        ftl=False,
        used=True,
        model_link='place_holder',
        description='Big black circle, causes destruction',
        stock=3,
        display_price=8500000,
        price_id=5
    )
    ship3 = Ship(
        name='Despot',
        manufacturer_id=1,
        category_id=1,
        display_size=8993,
        size_id=5,
        designer='Kr\'Andull',
        crew_id=4,
        range_id=3,
        ftl=True,
        used=False,
        model_link='place_holder',
        description='Big black circle, causes destruction',
        stock=3,
        display_price=15000000,
        price_id=5
    )
    ship4 = Ship(
        name='Star Talon',
        manufacturer_id=2,
        category_id=2,
        display_size=340,
        size_id=2,
        designer='Aren Bellee',
        crew_id=2,
        range_id=2,
        ftl=False,
        used=True,
        model_link='place_holder',
        description='Big black circle, causes destruction',
        stock=3,
        display_price=870000,
        price_id=4
    )
    ship5 = Ship(
        name='Proton',
        manufacturer_id=2,
        category_id=2,
        display_size=945,
        size_id=3,
        designer='Zach Rizer',
        crew_id=2,
        range_id=1,
        ftl=True,
        used=False,
        model_link='place_holder',
        description='Big black circle, causes destruction',
        stock=3,
        display_price=954000,
        price_id=4
    )
    ship6 = Ship(
        name='Trenxal',
        manufacturer_id=2,
        category_id=2,
        display_size=75,
        size_id=1,
        designer='Vlegi Moveloi',
        crew_id=1,
        range_id=5,
        ftl=False,
        used=True,
        model_link='place_holder',
        description='Big black circle, causes destruction',
        stock=3,
        display_price=657000,
        price_id=4
    )
    ship7 = Ship(
        name='The Rubber Ducky',
        manufacturer_id=3,
        category_id=3,
        display_size=9,
        size_id=1,
        designer='Ian Magenta',
        crew_id=1,
        range_id=1,
        ftl=True,
        used=True,
        model_link='place_holder',
        description='Big black circle, causes destruction',
        stock=3,
        display_price=3500,
        price_id=1
    )
    ship8 = Ship(
        name='The Æthelwulf',
        manufacturer_id=3,
        category_id=3,
        display_size=1212,
        size_id=4,
        designer='Take Mayuma',
        crew_id=3,
        range_id=3,
        ftl=False,
        used=True,
        model_link='place_holder',
        description='Big black circle, causes destruction',
        stock=3,
        display_price=8700,
        price_id=1
    )
    ship9 = Ship(
        name='Poseidon',
        manufacturer_id=3,
        category_id=3,
        display_size=7564,
        size_id=5,
        designer='Sui Gwu-Pao',
        crew_id=5,
        range_id=2,
        ftl=True,
        used=False,
        model_link='place_holder',
        description='Big black circle, causes destruction',
        stock=3,
        display_price=350000,
        price_id=3
    )
    ship10 = Ship(
        name='Apollo',
        manufacturer_id=4,
        category_id=4,
        display_size=765,
        size_id=3,
        designer='William Schraeder',
        crew_id=2,
        range_id=1,
        ftl=False,
        used=True,
        model_link='place_holder',
        description='Big black circle, causes destruction',
        stock=3,
        display_price=435000,
        price_id=3
    )
    ship11 = Ship(
        name='Oberon Nova',
        manufacturer_id=4,
        category_id=4,
        display_size=276,
        size_id=2,
        designer='Valdis Simril',
        crew_id=2,
        range_id=5,
        ftl=True,
        used=False,
        model_link='place_holder',
        description='Big black circle, causes destruction',
        stock=3,
        display_price=87000,
        price_id=2
    )
    ship12 = Ship(
        name='ISV Rimward Gold',
        manufacturer_id=4,
        category_id=4,
        display_size=764,
        size_id=3,
        designer='Guinevere Watrous',
        crew_id=2,
        range_id=4,
        ftl=False,
        used=True,
        model_link='place_holder',
        description='Big black circle, causes destruction',
        stock=3,
        display_price=96000,
        price_id=2
    )
    ship13 = Ship(
        name='Rimward Perseus',
        manufacturer_id=5,
        category_id=5,
        display_size=476,
        size_id=2,
        designer='Derrik Alder',
        crew_id=1,
        range_id=3,
        ftl=True,
        used=False,
        model_link='place_holder',
        description='Big black circle, causes destruction',
        stock=3,
        display_price=9999,
        price_id=1
    )
    ship14 = Ship(
        name='Tycho',
        manufacturer_id=5,
        category_id=5,
        display_size=89,
        size_id=1,
        designer='Maddox Volante',
        crew_id=1,
        range_id=2,
        ftl=False,
        used=True,
        model_link='place_holder',
        description='Big black circle, causes destruction',
        stock=3,
        display_price=650000,
        price_id=4
    )
    ship15 = Ship(
        name='The Leviathan',
        manufacturer_id=5,
        category_id=5,
        display_size=3745,
        size_id=4,
        designer='Abdullah Wafy',
        crew_id=4,
        range_id=1,
        ftl=True,
        used=False,
        model_link='place_holder',
        description='Big black circle, causes destruction',
        stock=3,
        display_price=956000,
        price_id=4
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
