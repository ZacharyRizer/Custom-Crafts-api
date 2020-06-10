import graphene
from graphene import Connection, Node, relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql_relay.node.node import from_global_id
from .filters import MyFilterableConnectionField
from .models import db, Category, Customer, Manufacturer, Ship, Order, OrderItem, Review
from .types import CategoryType, CustomerType, ManufacturerType, OrderType, OrderItemType, ReviewType, ShipType
from .auth import AuthError, requires_auth


class ShipNode(SQLAlchemyObjectType):
    class Meta:
        model = Ship
        connection_field_factory = MyFilterableConnectionField.factory


class ShipConnection(Connection):
    class Meta:
        node = ShipNode


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    categories = graphene.List(CategoryType)
    category = graphene.Field(
        CategoryType, category_id=graphene.ID(required=True))

    manufacturers = graphene.List(ManufacturerType)
    manufacturer = graphene.Field(
        ManufacturerType, manufacturer_id=graphene.ID(required=True))

    orders = graphene.List(OrderType)
    order = graphene.Field(
        OrderType, order_id=graphene.ID(required=True))

    order_items = graphene.List(OrderItemType)
    order_item = graphene.Field(
        OrderItemType, order_item_id=graphene.ID(required=True))

    reviews = graphene.List(ReviewType)
    review = graphene.Field(
        ReviewType, review_id=graphene.ID(required=True))

    ships = MyFilterableConnectionField(ShipConnection)  # uses filter
    ship = graphene.Field(
        ShipType, ship_id=graphene.ID(required=True))

    customers = graphene.List(CustomerType)
    customer = graphene.Field(
        CustomerType, customer_id=graphene.ID(required=True))

    def resolve_ship(self, info, ship_id):
        return Ship.query.get(ship_id)

    def resolve_categories(self, info, **kwargs):
        return Category.query.all()

    def resolve_category(self, info, category_id):
        return Category.query.get(category_id)

    def resolve_manufacturers(self, info, **kwargs):
        return Manufacturer.query.all()

    def resolve_manufacturer(self, info, manufacturer_id):
        return Manufacturer.query.get(manufacturer_id)

    def resolve_orders(self, info, **kwargs):
        return Order.query.all()

    def resolve_order(self, info, order_id):
        return Order.query.get(order_id)

    def resolve_order_items(self, info, **kwargs):
        return OrderItem.query.all()

    def resolve_order_item(self, info, order_item_id):
        return OrderItem.query.get(order_item_id)

    def resolve_reviews(self, info, **kwargs):
        return Review.query.all()

    def resolve_review(self, info, review_id):
        return Review.query.get(review_id)

    def resolve_customers(self, info, **kwargs):
        return Customer.query.all()

    def resolve_customer(self, info, customer_id):
        return Customer.query.get(customer_id)


# Mutations


class AddCustomer(graphene.Mutation):
    id = graphene.ID(required=True)
    name = graphene.String()
    email = graphene.String()
    auth0_id = graphene.String()

    class Arguments:
        name = graphene.String()
        email = graphene.String()
        auth0_id = graphene.String()

    @requires_auth
    def mutate(self, info, name, email, auth0_id):
        customer = Customer(name=name, email=email, auth0_id=auth0_id)
        db.session.add(customer)
        db.session.commit()

        return AddCustomer(
            id=customer.id,
            name=customer.name,
            email=customer.email,
            auth0_id=customer.auth0_id
        )


class AddOrder(graphene.Mutation):
    id = graphene.ID(required=True)
    customer_id = graphene.ID(required=True)

    class Arguments:
        customer_id = graphene.ID(required=True)

    def mutate(self, info, customer_id):
        order = Order(customer_id=customer_id)
        db.session.add(order)
        db.session.commit()

        return AddOrder(
            id=order.id,
            customer_id=order.customer_id)


class AddOrderItem(graphene.Mutation):
    id = graphene.ID(required=True)
    order_id = graphene.ID(required=True)
    ship_id = graphene.ID(required=True)
    quantity = graphene.Int()

    class Arguments:
        order_id = graphene.ID(required=True)
        ship_id = graphene.ID(required=True)
        quantity = graphene.Int()

    def mutate(self, info, order_id, ship_id, quantity):
        order_item = OrderItem(
            order_id=order_id, ship_id=ship_id, quantity=quantity)
        db.session.add(order_item)
        db.session.commit()

        return AddOrderItem(
            id=order_item.id,
            order_id=order_item.order_id,
            ship_id=order_item.ship_id,
            quantity=order_item.quantity
        )


class DeleteOrder(graphene.Mutation):
    id = graphene.ID(required=True)

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        db.session.delete(Order.query.get(id))
        db.session.commit()

        return DeleteOrder(id=id)


class DeleteOrderItem(graphene.Mutation):
    id = graphene.ID(required=True)

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        db.session.delete(OrderItem.query.get(id))
        db.session.commit()

        return DeleteOrderItem(id=id)


# class UpdateOrderItem(graphene.Mutation):
#     pass


class AddReview(graphene.Mutation):
    id = graphene.ID(required=True)
    customer_id = graphene.ID(required=True)
    ship_id = graphene.ID(required=True)
    rating = graphene.Int()
    description = graphene.String()

    class Arguments:
        customer_id = graphene.ID(required=True)
        ship_id = graphene.ID(required=True)
        rating = graphene.Int()
        description = graphene.String()

    def mutate(self, info, customer_id, ship_id, rating, description):
        review = Review(customer_id=customer_id, ship_id=ship_id,
                        rating=rating, description=description)
        db.session.add(review)
        db.session.commit()

        return AddReview(
            id=review.id,
            customer_id=review.customer_id,
            ship_id=review.ship_id,
            rating=review.rating,
            description=review.description
        )


class DeleteReview(graphene.Mutation):
    id = graphene.ID(required=True)

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        db.session.delete(Review.query.get(id))
        db.session.commit()

        return DeleteReview(id=id)


class Mutation(graphene.ObjectType):
    add_customer = AddCustomer.Field()
    add_order = AddOrder.Field()
    add_order_item = AddOrderItem.Field()
    delete_order = DeleteOrder.Field()
    delete_order_item = DeleteOrderItem.Field()
    add_review = AddReview.Field()
    delete_review = DeleteReview.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
