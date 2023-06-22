from django import template

from accessory.models import AccessoryCategory
from brides.models import BrideCategory
from dress.models import DressCategory

register = template.Library()


@register.simple_tag(name='get_dcatg')
def get_dresses_categories(filter=None):
    if not filter:
        return DressCategory.objects.all()
    else:
        return DressCategory.objects.filter(pk=filter)


@register.inclusion_tag('dress/list_dresses_categories.html')
def show_dresses_categories(sort=None, cat_selected=0):
    if not sort:
        return DressCategory.objects.all()
    else:
        dcatg = DressCategory.objects.extra(select={'length': 'Length(name)'}).order_by('-length')

    return {'dcatg': dcatg, 'cat_selected': cat_selected}


@register.simple_tag(name='get_acatg')
def get_accessories_categories(filter=None):
    if not filter:
        return AccessoryCategory.objects.all()
    else:
        return AccessoryCategory.objects.filter(pk=filter)


@register.inclusion_tag('accessory/list_accessories_categories.html')
def show_accessories_categories(sort=None, acat_selected=0):
    if not sort:
        return AccessoryCategory.objects.all()
    else:
        acatg = AccessoryCategory.objects.extra(select={'length': 'Length(name)'}).order_by('-length')

    return {'acatg': acatg, 'acat_selected': acat_selected}


@register.simple_tag(name='get_bcatg')
def get_brides_categories(filter=None):
    if not filter:
        return BrideCategory.objects.all()
    else:
        return BrideCategory.objects.filter(pk=filter)


@register.inclusion_tag('brides/list_brides_categories.html')
def show_brides_categories(sort=None, bcat_selected=0):
    if not sort:
        return BrideCategory.objects.all()
    else:
        bcatg = BrideCategory.objects.extra(select={'length': 'Length(name)'}).order_by('-length')

    return {'bcatg': bcatg, 'bcat_selected': bcat_selected}


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()
