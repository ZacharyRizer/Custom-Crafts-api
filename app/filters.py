from graphene_sqlalchemy_filter import FilterableConnectionField, FilterSet
from .models import Ship
# ALL_OPERATIONS = ['eq', 'ne', 'like', 'ilike', 'is_null', 'in', 'not_in', 'lt', 'lte', 'gt', 'gte', 'range']
OPERATIONS = ['eq', 'range']

class ShipFilter(FilterSet):
    class Meta:
        model = Ship
        fields = {
            "id": OPERATIONS,
            "manufacturer_id": OPERATIONS,
            "category_id": OPERATIONS,
            "ftl": OPERATIONS,
            "used": OPERATIONS,
        }


class MyFilterableConnectionField(FilterableConnectionField):
    filters = {Ship: ShipFilter()}