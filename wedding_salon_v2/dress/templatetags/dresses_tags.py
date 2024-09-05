from django import template

from dress.models import DressCategory

register = template.Library()


@register.simple_tag()
def show_dresses_categories():
    return DressCategory.objects.extra(select={'length': 'Length(title)'}).order_by('-length')
