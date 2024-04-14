from main.models import Category


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Category.objects.all()
        context['categories'] = categories
        if 'selected' not in context:
            context['selected'] = 0
        return context
