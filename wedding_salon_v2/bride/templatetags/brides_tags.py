from django import template
from django.db.models import Count

from bride.models import BrideCategory

register = template.Library()


@register.simple_tag()
def show_brides_categories():
    return BrideCategory.objects.annotate(bride_count=Count('bride')).filter(bride_count__gt=0).extra(select={'length': 'Length(bride_bridecategory.title)'}).order_by('-length')
