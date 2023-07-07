from django_filters import FilterSet

from mmorpg.models import Comment


class SearchFilter(FilterSet):
    class Meta:
        model = Comment
        fields = ['post_comment']
