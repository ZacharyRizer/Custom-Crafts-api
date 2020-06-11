from graphene_sqlalchemy_filter import FilterableConnectionField, FilterSet
from .models import Ship
# ALL_OPERATIONS = ['eq', 'ne', 'like', 'ilike', 'is_null', 'in', 'not_in', 'lt', 'lte', 'gt', 'gte', 'range']
OPERATIONS = ['eq', 'range', 'ilike']


class ShipFilter(FilterSet):
    class Meta:
        model = Ship
        fields = {
            "id": ['eq'],
            "category_id": ['eq'],
            "manufacturer_id": ['eq'],
            "crew_cap": ['range'],
            "size": ['range'],
            "travel_range": ['range'],
            "price": ['range'],
            "ftl": ['eq'],
            "used": ['eq'],
            "name": ['iLike']
        }


class MyFilterableConnectionField(FilterableConnectionField):
    filters = {Ship: ShipFilter()}
