from django_filters import rest_framework

from .models import Title


class CustomFilter(rest_framework.FilterSet):
    category = rest_framework.CharFilter(field_name='category__slug')
    genre = rest_framework.CharFilter(field_name='genre__slug')
    name = rest_framework.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Title
        fields = ('category', 'genre', 'year', 'name')
