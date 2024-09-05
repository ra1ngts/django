import django_filters
from django import forms

from .models import DressCategory, Color, Textile, Size, Dress


class SearchFilter(django_filters.FilterSet):
    cat = django_filters.ModelMultipleChoiceFilter(queryset=DressCategory.objects.all(),
                                                   widget=forms.CheckboxSelectMultiple,
                                                   label='Категория', )
    color = django_filters.ModelMultipleChoiceFilter(queryset=Color.objects.all(),
                                                     widget=forms.CheckboxSelectMultiple,
                                                     label='Цвет')
    textile = django_filters.ModelMultipleChoiceFilter(queryset=Textile.objects.all(),
                                                       widget=forms.CheckboxSelectMultiple,
                                                       label='Ткань')
    size = django_filters.ModelMultipleChoiceFilter(queryset=Size.objects.all(),
                                                    widget=forms.CheckboxSelectMultiple,
                                                    label='Размер')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Минимальная стоимость')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Максимальная стоимость')

    class Meta:
        model = Dress
        fields = ['cat', 'color', 'textile', 'size', 'min_price', 'max_price']
