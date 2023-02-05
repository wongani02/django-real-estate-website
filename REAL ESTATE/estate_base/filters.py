import django_filters
from django_filters import NumberFilter, CharFilter
from .models import *


class PropertyFilters(django_filters.FilterSet):
    property_name = CharFilter(field_name='property_name', lookup_expr='icontains')
    price = django_filters.NumberFilter()
    price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = HouseDetails
        fields = ['status', 'number_of_bedrooms',  'location', 'number_of_bathrooms',
                  'district']
