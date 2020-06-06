import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

# class TestObj(graphene.ObjectType):
#     title = graphene.String()
#     description = graphene.String()
#     age = graphene.Int()


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.Argument(
        graphene.String, default_value='stranger'),
        age=graphene.Argument(graphene.Int))

    def resolve_hello(self, info, **args):
        return f'Hello {args["name"]}, you are {args["age"]} years old!'


schema = graphene.Schema(query=Query)
