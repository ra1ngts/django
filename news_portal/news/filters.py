import django_filters
from django_filters import FilterSet
from django_filters.widgets import RangeWidget

from news.models import Author


class SearchFilter(FilterSet):
    author_post = django_filters.ModelChoiceFilter(queryset=Author.objects.all(), label='Автор',
                                                   empty_label='Не выбран')
    title = django_filters.CharFilter(field_name='title_post', lookup_expr='icontains', label='Заголовок')
    date = django_filters.DateFromToRangeFilter(field_name='date_post', widget=RangeWidget(attrs={'type': 'date'}),
                                                label='Дата')
