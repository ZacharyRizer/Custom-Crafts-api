import graphene
from graphene import Connection, Node, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from .models import db, Category, Customer, Manufacturer, Ship, Order, OrderItem, Review


class ShipType(SQLAlchemyObjectType):
    class Meta:
        model = Ship


class CategoryType(SQLAlchemyObjectType):
    class Meta:
        model = Category


class CustomerType(SQLAlchemyObjectType):
    class Meta:
        model = Customer


class ManufacturerType(SQLAlchemyObjectType):
    class Meta:
        model = Manufacturer


class OrderType(SQLAlchemyObjectType):
    class Meta:
        model = Order


class OrderItemType(SQLAlchemyObjectType):
    class Meta:
        model = OrderItem


class ReviewType(SQLAlchemyObjectType):
    class Meta:
        model = Review
