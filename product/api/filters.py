from django_filters import rest_framework as filters
from product.models import Product


class BrowseProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_rent = filters.NumberFilter(field_name="rent", lookup_expr='gte')
    max_rent = filters.NumberFilter(field_name="rent", lookup_expr='lte')
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ('name', 'categories', 'rent_type',
                  'is_for_sell', 'is_for_rent')
