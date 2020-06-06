import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from .models import Manufacturer

# class TestObj(graphene.ObjectType):
#     title = graphene.String()
#     description = graphene.String()
#     age = graphene.Int()


class ManufacturerType(SQLAlchemyObjectType):
    class Meta:
        model = Manufacturer
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # manufacturers = SQLAlchemyConnectionField(Manufacturer.connection)
    manufacturers = graphene.List(ManufacturerType)
    manufacturer = graphene.Field(
        ManufacturerType, manufacturer_id=graphene.Int())

    def resolve_manufacturers(self, info, **kwargs):
        return Manufacturer.query.all()

    def resolve_manufacturer(self, info, manufacturer_id):
        return Manufacturer.query.get(manufacturer_id)
    # hello = graphene.String(name=graphene.Argument(
    #     graphene.String, default_value='stranger'),
    #     age=graphene.Argument(graphene.Int))

    # def resolve_hello(self, info, **args):
    #     return f'Hello {args["name"]}, you are {args["age"]} years old!'


schema = graphene.Schema(query=Query)
