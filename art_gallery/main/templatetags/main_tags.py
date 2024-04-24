from django import template
from django.db.models import Count

from main.models import Category

register = template.Library()


@register.simple_tag
def get_categories(filter=None):
    if not filter:
        return Category.objects.annotate(Count('gallery'))
    else:
        return Category.objects.filter(pk=filter)
