from dataclasses import field
from django_filters import rest_framework as filters
from .models import Menu

class MenuFilter(filters.FilterSet):
    keyword = filters.CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Menu
        fields = ('name', 'price')