import django_filters
from django_filters import FilterSet
from django_filters.widgets import RangeWidget

from news.models import Author
from django.utils.translation import gettext_lazy as _


class SearchFilter(FilterSet):
    author_post = django_filters.ModelChoiceFilter(queryset=Author.objects.all(), label=_('Автор'),
                                                   empty_label=_('Не выбран'))
    title = django_filters.CharFilter(field_name='title_post', lookup_expr='icontains', label=_('Заголовок'))
    date = django_filters.DateFromToRangeFilter(field_name='date_post', widget=RangeWidget(attrs={'type': 'date'}),
                                                label=_('Дата'))
