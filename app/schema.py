import graphene
from graphene import Connection, Node
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene_sqlalchemy_filter import FilterSet, FilterableConnectionField
from sqlalchemy.sql import text

from .models import db, Category, Customer, Manufacturer, Ship, Order, OrderItem, Review
from .auth import AuthError, requires_auth


ALL_OPERATIONS = ['eq', 'ne', 'like', 'ilike', 'is_null', 'in', 'not_in', 'lt', 'lte', 'gt', 'gte', 'range']

class ShipFilter(FilterSet):
    class Meta:
        model = Ship
        fields = {
            "id": ALL_OPERATIONS,
            "manufacturer_id": ALL_OPERATIONS,
            "category_id": ALL_OPERATIONS,
            "ftl": ALL_OPERATIONS,
            "used": ALL_OPERATIONS,
        }


class MyFilterableConnectionField(FilterableConnectionField):
    filters = {Ship: ShipFilter()}

class ShipNode(SQLAlchemyObjectType):
    class Meta:
        model = Ship
        interfaces = (Node,)
        connection_field_factory = MyFilterableConnectionField.factory


class ShipConnection(Connection):
    class Meta:
        node = ShipNode


class Query(graphene.ObjectType):
    ship = graphene.relay.Node.Field(ShipNode)
    all_ships = MyFilterableConnectionField(ShipConnection)

schema = graphene.Schema(query=Query)
