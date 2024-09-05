from django import template

from accessory.models import AccessoryCategory

register = template.Library()


@register.simple_tag()
def show_accessories_categories():
    return AccessoryCategory.objects.extra(select={'length': 'Length(title)'}).order_by('-length')
