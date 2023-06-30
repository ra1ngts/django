from rest_framework import serializers

from news.models import Post


class NewsArticleSerializer(serializers.ModelSerializer):
    author_post = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'
