import graphene
from graphene import Connection, Node, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from .models import db, Category, Customer, Manufacturer, Ship, Order, OrderItem, Review

class ShipType(SQLAlchemyObjectType):
    class Meta:
        model = Ship
        interfaces = (relay.Node, )


class CategoryType(SQLAlchemyObjectType):
    class Meta:
        model = Category
        interfaces = (relay.Node, )


class CustomerType(SQLAlchemyObjectType):
    class Meta:
        model = Customer
        # Research following line, possibly unnecessary in all _Type Classes.
        interfaces = (relay.Node, )


class ManufacturerType(SQLAlchemyObjectType):
    class Meta:
        model = Manufacturer
        interfaces = (relay.Node, )


class OrderType(SQLAlchemyObjectType):
    class Meta:
        model = Order
        interfaces = (relay.Node, )


class OrderItemType(SQLAlchemyObjectType):
    class Meta:
        model = OrderItem
        interfaces = (relay.Node, )


class ReviewType(SQLAlchemyObjectType):
    class Meta:
        model = Review
        interfaces = (relay.Node, )