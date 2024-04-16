class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        if 'selected' not in context:
            context['selected'] = 0
        return context
