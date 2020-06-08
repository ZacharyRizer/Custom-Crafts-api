import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from .models import db, Customer, Manufacturer, Ship
from .auth import AuthError, requires_auth


# class TestObj(graphene.ObjectType):
#     title = graphene.String()
#     description = graphene.String()
#     age = graphene.Int()


class CustomerType(SQLAlchemyObjectType):
    class Meta:
        model = Customer
        # Research following line, possibly unnecessary in all _Type Classes.
        interfaces = (relay.Node, )


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

    # ships

    ships = graphene.List(ShipType)
    ship = graphene.Field(
        ShipType, ship_id=graphene.Int())

    # customers

    customers = graphene.List(CustomerType)
    customer = graphene.Field(
        CustomerType, customer_id=graphene.Int())

    def resolve_manufacturers(self, info, **kwargs):
        return Manufacturer.query.all()

    def resolve_manufacturer(self, info, manufacturer_id):
        return Manufacturer.query.get(manufacturer_id)

    def resolve_ships(self, info, **kwargs):
        return Ship.query.all()

# Add **kwargs to all single instance resolvers as well?
    def resolve_ship(self, info, ship_id):
        return Ship.query.get(ship_id)

    def resolve_customers(self, info, **kwargs):
        return Customer.query.all()

    def resolve_customer(self, info, customer_id):
        return Customer.query.get(customer_id)

    # Mutations


class AddCustomer(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()

    class Arguments:
        name = graphene.String()
        email = graphene.String()

    def mutate(self, info, name, email):
        customer = Customer(name=name, email=email)
        db.session.add(customer)
        db.session.commit()

        return AddCustomer(
            id=customer.id,
            name=customer.name,
            email=customer.email
        )


class Mutation(graphene.ObjectType):
    add_customer = AddCustomer.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
