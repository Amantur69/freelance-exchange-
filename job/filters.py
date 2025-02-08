from datetime import timezone, timedelta

import django_filters
from .models import *


class ServiceFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter(field_name='price', lookup_expr='exact')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Service
        fields = ['price', 'price_min', 'price_max']




