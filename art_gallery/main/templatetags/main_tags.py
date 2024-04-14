# from django import template
#
# from main.models import Category
#
# register = template.Library()
#
#
# @register.simple_tag
# def get_categories(filter=None):
#     if not filter:
#         return Category.objects.all()
#     else:
#         return Category.objects.filter(pk=filter)
