class DataMixin:
    def get_mixin_context(self, context, **kwargs):
        context['title'] = None
        context.update(kwargs)
        return context
