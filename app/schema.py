import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from .models import Manufacturer, Ship

# class TestObj(graphene.ObjectType):
#     title = graphene.String()
#     description = graphene.String()
#     age = graphene.Int()


class ManufacturerType(SQLAlchemyObjectType):
    class Meta:
        model = Manufacturer
        interfaces = (relay.Node, )


class ShipType(SQLAlchemyObjectType):
    class Meta:
        model = Ship
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # manufacturers = SQLAlchemyConnectionField(Manufacturer.connection)
    manufacturers = graphene.List(ManufacturerType)
    manufacturer = graphene.Field(
        ManufacturerType, manufacturer_id=graphene.Int())

    ships = graphene.List(ShipType)
    ship = graphene.Field(
        ShipType, ship_id=graphene.Int())

    def resolve_manufacturers(self, info, **kwargs):
        return Manufacturer.query.all()

    def resolve_manufacturer(self, info, manufacturer_id):
        return Manufacturer.query.get(manufacturer_id)

    def resolve_ships(self, info, **kwargs):
        return Ship.query.all()

    def resolve_ship(self, info, ship_id):
        return Ship.query.get(ship_id)


schema = graphene.Schema(query=Query)
