from app.models import Ship, db
from app import create_app
from dotenv import load_dotenv
load_dotenv()

app = create_app()

with app.app_context():

    ship1 = Ship.query.get(1)
    ship1.name = 'Ship_Path_Example'
    ship2 = Ship.query.get(2)
    ship2.name = 'Ship_Path_Example'
    ship3 = Ship.query.get(3)
    ship3.name = 'Ship_Path_Example'
    ship4 = Ship.query.get(4)
    ship4.name = 'Ship_Path_Example'
    ship5 = Ship.query.get(5)
    ship5.name = 'Ship_Path_Example'
    ship6 = Ship.query.get(6)
    ship6.name = 'Ship_Path_Example'
    ship7 = Ship.query.get(7)
    ship7.name = 'Ship_Path_Example'
    ship8 = Ship.query.get(8)
    ship8.name = 'Ship_Path_Example'
    ship9 = Ship.query.get(9)
    ship9.name = 'Ship_Path_Example'
    ship10 = Ship.query.get(10)
    ship10.name = 'Ship_Path_Example'
    ship11 = Ship.query.get(11)
    ship11.name = 'Ship_Path_Example'
    ship12 = Ship.query.get(12)
    ship12.name = 'Ship_Path_Example'
    ship13 = Ship.query.get(13)
    ship13.name = 'Ship_Path_Example'
    ship14 = Ship.query.get(14)
    ship14.name = 'Ship_Path_Example'
    ship15 = Ship.query.get(15)
    ship15.name = 'Ship_Path_Example'
    ship16 = Ship.query.get(16)
    ship16.name = 'Ship_Path_Example'
    ship17 = Ship.query.get(17)
    ship17.name = 'Ship_Path_Example'
    ship18 = Ship.query.get(18)
    ship18.name = 'Ship_Path_Example'
    ship19 = Ship.query.get(19)
    ship19.name = 'Ship_Path_Example'
    ship20 = Ship.query.get(20)
    ship20.name = 'Ship_Path_Example'

    db.session.commit()

    print('finish updating model path')