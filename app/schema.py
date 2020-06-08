import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from .models import db, Customer, Manufacturer, Ship, Category, Order, OrderItem, Review
from .auth import AuthError, requires_auth


# class TestObj(graphene.ObjectType):
#     title = graphene.String()
#     description = graphene.String()
#     age = graphene.Int()

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


class ShipType(SQLAlchemyObjectType):
    class Meta:
        model = Ship
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    # categories

    categories = graphene.List(CategoryType)
    category = graphene.Field(
        CategoryType, category_id=graphene.Int())

    # manufacturers = SQLAlchemyConnectionField(Manufacturer.connection)

    manufacturers = graphene.List(ManufacturerType)
    manufacturer = graphene.Field(
        ManufacturerType, manufacturer_id=graphene.Int())

    # orders

    orders = graphene.List(OrderType)
    order = graphene.Field(
        OrderType, order_id=graphene.Int())

    # order-items

    order_items = graphene.List(OrderItemType)
    order_item = graphene.Field(
        OrderItemType, order_item_id=graphene.Int())

    # reviews
    reviews = graphene.List(ReviewType)
    review = graphene.Field(
        ReviewType, review_id=graphene.Int())

    # ships

    ships = graphene.List(ShipType)
    ship = graphene.Field(
        ShipType, ship_id=graphene.Int())

    # customers

    customers = graphene.List(CustomerType)
    customer = graphene.Field(
        CustomerType, customer_id=graphene.Int())

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


class AddOrder(graphene.Mutation):
    id = graphene.Int()
    customer_id = graphene.Int()

    class Arguments:
        customer_id = graphene.Int()

    def mutate(self, info, customer_id):
        order = Order(customer_id=customer_id)
        db.session.add(order)
        db.session.commit()

        return AddOrder(
            id=order.id
            customer_id=order.customer_id
        )


class AddOrderItem(graphene.Mutation):
    id = graphene.Int()
    order_id = graphene.Int()
    ship_id = graphene.Int()
    quantity = graphene.Int()

    class Arguments:
        order_id = graphene.Int()
        ship_id = graphene.Int()
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


class AddReview(graphene.Mutation):
    id = graphene.Int()
    customer_id = graphene.Int()
    ship_id = graphene.Int()
    rating = graphene.Int()
    description = graphene.String()

    class Arguments:
        customer_id = graphene.Int()
        ship_id = graphene.Int()
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


class Mutation(graphene.ObjectType):
    add_customer = AddCustomer.Field()
    add_review = AddReview.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
