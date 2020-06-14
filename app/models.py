from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Ship(db.Model):
    __tablename__ = 'ships'

    id = db.Column(db.Integer, primary_key=True)  # autoincrement=True
    name = db.Column(db.String(50), nullable=False, unique=True)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey(
        'manufacturers.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'categories.id'), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    designer = db.Column(db.String(50), nullable=False)
    crew_cap = db.Column(db.Integer, nullable=False)
    travel_range = db.Column(db.Integer, nullable=False)
    ftl = db.Column(db.Boolean, nullable=False)
    used = db.Column(db.Boolean, nullable=False)
    model_link = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    stock = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    total_sold = db.Column(db.Integer)

    manufacturer = db.relationship('Manufacturer', back_populates='ships')
    category = db.relationship('Category', back_populates='ships')
    order_items = db.relationship('OrderItem', back_populates='ship')
    reviews = db.relationship('Review', back_populates='ship')


class Manufacturer(db.Model):
    __tablename__ = 'manufacturers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    ships = db.relationship('Ship', back_populates='manufacturer')


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    ships = db.relationship('Ship', back_populates='category')


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    auth0_id = db.Column(db.String, unique=True)
    picture = db.Column(db.String)

    orders = db.relationship('Order', back_populates='customer')
    reviews = db.relationship('Review', back_populates='customer')


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey(
        'customers.id'), nullable=False)

    customer = db.relationship('Customer', back_populates='orders')
    order_items = db.relationship('OrderItem', back_populates='order')


class OrderItem(db.Model):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(
        'orders.id'), nullable=False)
    ship_id = db.Column(db.Integer, db.ForeignKey('ships.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String)
    created_at = db.Column(db.DateTime)

    order = db.relationship('Order', back_populates='order_items')
    ship = db.relationship('Ship', back_populates='order_items')


class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey(
        'customers.id'), nullable=False)
    ship_id = db.Column(db.Integer, db.ForeignKey('ships.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String)
    upVoteCount = db.Column(db.Integer)
    downVoteCount = db.Column(db.Integer)

    customer = db.relationship('Customer', back_populates='reviews')
    ship = db.relationship('Ship', back_populates='reviews')
