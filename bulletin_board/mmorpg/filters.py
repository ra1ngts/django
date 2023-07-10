from django_filters import FilterSet

from mmorpg.models import Post


class SearchFilter(FilterSet):
    class Meta:
        model = Post
        fields = ['category_post', 'title_post']
