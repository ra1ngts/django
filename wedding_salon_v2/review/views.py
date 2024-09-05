from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ReviewForm
from .models import Review
from services.utils import DataMixin


class Reviews(DataMixin, CreateView):
    model = Review
    template_name = 'review/index.html'
    context_object_name = 'reviews'
    form_class = ReviewForm
    success_url = reverse_lazy('reviews')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.filter(is_published=True)
        paginator = Paginator(reviews, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return self.get_mixin_context(context, title='Отзывы')

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Спасибо за отзыв. Мы опубликуем его в ближайшее время.',
                             extra_tags='review')
        return super().form_valid(form)
