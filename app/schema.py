import graphene
from graphene import Connection, Node, relay
from graphene_sqlalchemy import SQLAlchemyObjectType
import threading
import json
import datetime

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
        CategoryType, category_id=graphene.Int())

    manufacturers = graphene.List(ManufacturerType)
    manufacturer = graphene.Field(
        ManufacturerType, manufacturer_id=graphene.Int())

    orders = graphene.List(OrderType)
    order = graphene.Field(
        OrderType, order_id=graphene.Int())

    order_items = graphene.List(OrderItemType)
    order_item = graphene.Field(
        OrderItemType, order_item_id=graphene.Int())

    reviews = graphene.List(ReviewType)
    review = graphene.Field(
        ReviewType, review_id=graphene.Int())

    ships = MyFilterableConnectionField(ShipConnection)  # uses filter
    ship = graphene.Field(
        ShipType, ship_id=graphene.Int())

    customers = graphene.List(CustomerType)
    customer = graphene.Field(
        CustomerType, customer_id=graphene.Int())

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
        print('resolve_order')
        return Order.query.get(order_id)

    def resolve_order_items(self, info, **kwargs):
        print('resolve order_items')
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
        print('customer resolver')
        return Customer.query.get(customer_id)


# Mutations


class AddCustomer(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()
    auth0_id = graphene.String()
    picture = graphene.String()

    class Arguments:
        name = graphene.String()
        email = graphene.String()
        auth0_id = graphene.String()
        picture = graphene.String()

    @requires_auth
    def mutate(self, info, name, email, auth0_id, picture):
        customer = Customer.query.filter(Customer.email == email).first()
        if customer:
            customer.name = name
            customer.email = email
            customer.auth0_id = auth0_id
            customer.picture = picture
        else:
            customer = Customer(name=name, email=email,
                                auth0_id=auth0_id, picture=picture)
            db.session.add(customer)
        db.session.commit()

        return AddCustomer(
            id=customer.id,
            name=customer.name,
            email=customer.email,
            auth0_id=customer.auth0_id,
            picture=customer.picture
        )


# class ItemInputType(graphene.InputObjectType):
#     ship_id = graphene.Int(required=True)
#     quantity = graphene.Int(required=True)


class OrderItemInputType(graphene.InputObjectType):
    customer_id = graphene.Int()
    items = graphene.JSONString()
    # ship_id = graphene.Int(required=True)
    # quantity = graphene.Int(required=True)


class AddOrder(graphene.Mutation):
    id = graphene.Int()
    cart = graphene.Field(OrderItemType)

    class Arguments:
        cart = graphene.Argument(OrderItemInputType)

    def mutate(self, info, cart):
        order = Order(customer_id=cart.customer_id)

        def makeOrderItem(order, item):
            order_item = OrderItem(
                order_id=order.id,
                ship_id=item['shipId'],
                quantity=item['quantity'],
                color=item['color'],
                created_at=datetime.datetime.now())
            db.session.add(order_item)
            db.session.commit()

        def incrementStockLocal(shipId):
            print(f'shipId {shipId}')
            # shipI = Ship.query.get(shipId)
            # print('in incrementStockLocal')
            # shipI.stock += 4
            # db.session.commit()

        def decrementStockLocal(item):
            ship = Ship.query.get(item['shipId'])
            ship.stock -= item['quantity']

            # adjust total sold

            ship.total_sold += item['quantity']

            db.session.commit()
            print(f'before if, ship.stock')
            if ship.stock == 0:
                # print('creating asyncio loop obj')
                # loop = asyncio.new_event_loop()
                # asyncio.set_event_loop(loop)
                # loop.call_later(8, incrementStockLocal, ship)
                # loop.run_until_complete()
                # loop.close()

                t = threading.Timer(8, incrementStockLocal, ([ship.id]))
                t.start()
                db.session.commit()

        db.session.add(order)
        db.session.commit()

        # loop through cart

        for item in cart.items:
            makeOrderItem(order, item)
            decrementStockLocal(item)

        # db.session.commit()

        return AddOrder(
            id=order.id)
        # customer_id=order.customer_id)


# class AddOrderItem(graphene.Mutation):
#     print('orderItem mutation')

#     id = graphene.Int()
#     order_id = graphene.Int()
#     ship_id = graphene.Int()
#     quantity = graphene.Int()

#     class Arguments:
#         order_id = graphene.Int()
#         ship_id = graphene.Int()
#         quantity = graphene.Int()

#     @requires_auth
#     def mutate(self, info, order_id, ship_id, quantity):
#         order_item = OrderItem(
#             order_id=order_id, ship_id=ship_id, quantity=quantity)
#         db.session.add(order_item)
#         db.session.commit()

#         return AddOrderItem(
#             id=order_item.id,
#             order_id=order_item.order_id,
#             ship_id=order_item.ship_id,
#             quantity=order_item.quantity
#         )


class IncrementShipStock(graphene.Mutation):
    id = graphene.Int()
    stock = graphene.Int()

    class Arguments:
        id = graphene.Int()
        inc_quantity = graphene.Int()

    def mutate(self, info, id, inc_quantity):
        ship = Ship.query.get(id)
        ship.stock += inc_quantity
        db.session.commit()

        return IncrementShipStock(
            id=id,
            stock=ship.stock
        )


class DecrementShipStock(graphene.Mutation):
    id = graphene.Int()
    stock = graphene.Int()

    class Arguments:
        id = graphene.Int()
        dec_quantity = graphene.Int()

    @requires_auth
    def mutate(self, info, id, dec_quantity):
        print(f'self {self}')
        ship = Ship.query.get(id)
        ship.stock -= dec_quantity

        db.session.commit()

        # if ship.stock == 0:
        #     t = threading.Timer(20, self.upStock)
        #     t.start()

        # test = Timer(300, (lambda:print('testing')))

        return DecrementShipStock(
            id=id,
            stock=ship.stock
        )


class DeleteOrder(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    @requires_auth
    def mutate(self, info, id):
        db.session.delete(Order.query.get(id))
        db.session.commit()

        return DeleteOrder(id=id)


class DeleteOrderItem(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    @requires_auth
    def mutate(self, info, id):
        db.session.delete(OrderItem.query.get(id))
        db.session.commit()

        return DeleteOrderItem(id=id)


# class UpdateOrderItem(graphene.Mutation):
#     pass


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

    # @requires_auth
    def mutate(self, info, customer_id, ship_id, rating, description):
        review = Review(customer_id=customer_id, ship_id=ship_id,
                        rating=rating, description=description)
        customer = Customer.query.get(customer_id)
        db.session.add(review)
        db.session.commit()

        return AddReview(
            id=review.id,
            customer=review.customer,
            ship_id=review.ship_id,
            rating=review.rating,
            description=review.description
        )


class DeleteReview(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    # @requires_auth
    def mutate(self, info, id):
        db.session.delete(Review.query.get(id))
        db.session.commit()

        return DeleteReview(id=id)


class Mutation(graphene.ObjectType):
    add_customer = AddCustomer.Field()
    add_order = AddOrder.Field()
    # add_order_item = AddOrderItem.Field()
    delete_order = DeleteOrder.Field()
    delete_order_item = DeleteOrderItem.Field()
    add_review = AddReview.Field()
    delete_review = DeleteReview.Field()
    decrement_ship_stock = DecrementShipStock.Field()
    increment_ship_stock = IncrementShipStock.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
