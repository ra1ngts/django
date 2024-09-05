from django import template
from django.urls import resolve, Resolver404

register = template.Library()


@register.simple_tag
def active(request, url_name):
    try:
        if resolve(request.path_info).url_name == url_name:
            return 'active'
    except Resolver404:
        return ''
    return ''


@register.simple_tag(takes_context=True)
def active_dropdown(context, request, *args):
    current_path = request.path
    for arg in args:
        if arg in current_path:
            return 'active'
    return ''
