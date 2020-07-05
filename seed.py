from app.models import Manufacturer, Ship, Category, db
from app import create_app
from dotenv import load_dotenv
load_dotenv()

# size 1 = 100, 100-500, 500-1000, 1000-5000, 5000+
# price = 100, 100-1000, 1000-10000, 10000-100000, 100000+
# range = 25, 25-100, 100-1000, 1000-10000, 10000+
# crew_cap = 10, 10-100, 100-500, 500-1000, 1000+

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    man1 = Manufacturer(id=1, name='Imperial Galactic Government')
    man2 = Manufacturer(id=2, name='Spacing Guild')
    man3 = Manufacturer(id=3, name='Corellian Engineering Corporation')
    man4 = Manufacturer(id=4, name='Cybertronian Technologies')
    man5 = Manufacturer(id=5, name='Weyland-Yutani Corporation')
    cat1 = Category(id=1, name='Military')
    cat2 = Category(id=2, name='Transport')
    cat3 = Category(id=3, name='Cargo')
    cat4 = Category(id=4, name='Performance')
    cat5 = Category(id=5, name='Luxury')

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
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship1_green.glb',
        description='Big black circle, causes destruction',
        stock=3,
        total_sold=0,
        price=470000
    )
    ship2 = Ship(
        name='SS Dreadnought',
        manufacturer_id=1,
        category_id=2,
        size=4788,
        designer='Glama V\'Leeni',
        crew_cap=1000,
        travel_range=9500,
        ftl=False,
        used=True,
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship2_red.glb',
        description='Big black circle, causes destruction',
        stock=3,
        total_sold=0,
        price=850000
    )
    ship3 = Ship(
        name='Despot',
        manufacturer_id=1,
        category_id=3,
        size=8993,
        designer='Kr\'Andull',
        crew_cap=500,
        travel_range=8700,
        ftl=True,
        used=False,
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship3_orange.glb',
        description='Tyrannical cruiser that dictates its will upon all other spacecrafts',
        stock=3,
        total_sold=0,
        price=150000
    )
    ship4 = Ship(
        name='Star Talon',
        manufacturer_id=2,
        category_id=4,
        size=340,
        designer='Aren Bellee',
        crew_cap=350,
        travel_range=850,
        ftl=False,
        used=True,
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship4_blue.glb',
        description='Scintillating through space, grasping unlicensed prey',
        stock=3,
        total_sold=0,
        price=8700
    )
    ship5 = Ship(
        name='Proton',
        manufacturer_id=2,
        category_id=5,
        size=945,
        designer='Zach Rizer',
        crew_cap=10,
        travel_range=13000,
        ftl=True,
        used=False,
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship5_red.glb',
        description='Positive force of Yang',
        stock=3,
        total_sold=0,
        price=23000
    )
    ship6 = Ship(
        name='Trenxal',
        manufacturer_id=2,
        category_id=1,
        size=86,
        designer='Abdullah Wafy',
        crew_cap=50,
        travel_range=90,
        ftl=False,
        used=True,
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship6_blue.glb',
        description='The flying buzzer scanning for intruders',
        stock=3,
        total_sold=0,
        price=657
    )
    ship7 = Ship(
        name='The Rubber Ducky',
        manufacturer_id=3,
        category_id=2,
        size=10,
        designer='Ian Magenta',
        crew_cap=2,
        travel_range=23,
        ftl=True,
        used=False,
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship7_orange.glb',
        description="Ian\'s favorite toy as a little kid",
        stock=3,
        total_sold=0,
        price=75
    )
    ship8 = Ship(
        name='The Æthelwulf',
        manufacturer_id=3,
        category_id=3,
        size=1212,
        designer='Take Mayuma',
        crew_cap=50,
        travel_range=10,
        ftl=False,
        used=True,
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship8_green.glb',
        description='Royal ambitions with medieval interior design',
        stock=3,
        total_sold=0,
        price=67000
    )
    ship9 = Ship(
        name='Poseidon',
        manufacturer_id=3,
        category_id=4,
        size=7564,
        designer='Sui Gwu-Pao',
        crew_cap=1200,
        travel_range=5800,
        ftl=True,
        used=False,
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship9_orange.glb',
        description='Rule the oceans of space as you swim through orbits',
        stock=3,
        total_sold=0,
        price=8900
    )
    ship10 = Ship(
        name='Apollo',
        manufacturer_id=4,
        category_id=5,
        size=765,
        designer='William Schraeder',
        crew_cap=300,
        travel_range=3500,
        ftl=False,
        used=True,
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship10_red.glb',
        description='To the Moon and beyond! Robust structure resists solar flares',
        stock=3,
        total_sold=0,
        price=435
    )
    ship11 = Ship(
        name='Oberon Nova',
        manufacturer_id=4,
        category_id=1,
        size=276,
        designer='Abdullah Wafy',
        crew_cap=100,
        travel_range=4500,
        ftl=True,
        used=False,
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship11_blue.glb',
        description='Tour the galaxies with the authentic merkaba',
        stock=3,
        total_sold=0,
        price=8700
    )
    ship12 = Ship(
        name='ISV Rimward Gold',
        manufacturer_id=4,
        category_id=2,
        size=764,
        designer='Guinevere Watrous',
        crew_cap=250,
        travel_range=900,
        ftl=False,
        used=True,
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship12_green.glb',
        description='Gold-plated surfaces abound',
        stock=3,
        total_sold=0,
        price=96000
    )
    ship13 = Ship(
        name='DH Enterprise',
        manufacturer_id=5,
        category_id=3,
        size=476,
        designer='Derrik Alder',
        crew_cap=100,
        travel_range=5700,
        ftl=True,
        used=False,
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship13_green.glb',
        description='For hikers through star trails',
        stock=3,
        total_sold=0,
        price=9000
    )
    ship14 = Ship(
        name='Tycho',
        manufacturer_id=5,
        category_id=4,
        size=156,
        designer='Maddox Volante',
        crew_cap=50,
        travel_range=7500,
        ftl=False,
        used=True,
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship14_red.glb',
        description='Discover frontiers of the beyond',
        stock=3,
        total_sold=0,
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
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship15_blue.glb',
        description='Mysterious deep-space monster of a ship dominating all others...',
        stock=3,
        total_sold=0,
        price=999999
    )
    ship16 = Ship(
        name='Pegasus',
        manufacturer_id=5,
        category_id=5,
        size=3745,
        designer='Abdullah Wafy',
        crew_cap=1000,
        travel_range=12000,
        ftl=True,
        used=False,
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship16_orange.glb',
        description='For those with a heroic bent. Fly at will with lightning speed.',
        stock=3,
        total_sold=0,
        price=999999
    )
    ship17 = Ship(
        name='Seraph',
        manufacturer_id=5,
        category_id=5,
        size=3745,
        designer='Abdullah Wafy',
        crew_cap=1000,
        travel_range=12000,
        ftl=True,
        used=False,
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship17_green.glb',
        description='Exalted design with superb flight power',
        stock=3,
        total_sold=0,
        price=999999
    )
    ship18 = Ship(
        name='Angel',
        manufacturer_id=5,
        category_id=5,
        size=3745,
        designer='Abdullah Wafy',
        crew_cap=1000,
        travel_range=12000,
        ftl=True,
        used=False,
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship18_red.glb',
        description='Infinity pool inside in a Utopian setting',
        stock=3,
        total_sold=0,
        price=999999
    )
    ship19 = Ship(
        name='The Milano',
        manufacturer_id=5,
        category_id=5,
        size=3745,
        designer='Valdis Simril',
        crew_cap=1000,
        travel_range=12000,
        ftl=True,
        used=False,
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship19_blue.glb',
        description='Crush it, smash it, own it',
        stock=3,
        total_sold=0,
        price=999999
    )
    ship20 = Ship(
        name='Mutation',
        manufacturer_id=5,
        category_id=5,
        size=3745,
        designer='Vlegi Moveloi',
        crew_cap=1000,
        travel_range=12000,
        ftl=True,
        used=False,
        model_link='https://custom-crafts-inventory.s3-us-west-1.amazonaws.com/spaceships/ship20_orange.glb',
        description='Malignant spread, not for benign folks',
        stock=3,
        total_sold=0,
        price=999999
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
    db.session.add(ship16)
    db.session.add(ship17)
    db.session.add(ship18)
    db.session.add(ship19)
    db.session.add(ship20)

    db.session.commit()

    print('finish seed')
