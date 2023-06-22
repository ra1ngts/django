import django_filters
from django_filters import FilterSet

from dress.models import DressCategory, Color, Textile, Size


class SearchFilter(FilterSet):
    color = django_filters.ModelMultipleChoiceFilter(queryset=Color.objects.all(), label='Цвет')
    textile = django_filters.ModelMultipleChoiceFilter(queryset=Textile.objects.all(), field_name='textile',
                                                       label='Ткань')
    size = django_filters.ModelMultipleChoiceFilter(queryset=Size.objects.all(), field_name='size', label='Размер')
    price = django_filters.AllValuesMultipleFilter(field_name='price', label='Цена')
    cat = django_filters.ModelMultipleChoiceFilter(queryset=DressCategory.objects.all(), label='Категория')
