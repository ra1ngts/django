from django.contrib import admin

from mmorpg.models import Category, Post, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('author_post', 'title_post', 'text_post', 'category_post', 'date_post')
    list_display_links = ('author_post', 'title_post', 'category_post')
    list_filter = ('author_post', 'title_post', 'category_post', 'date_post')
    search_fields = ('author_post', 'title_post', 'category_post', 'date_post')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_comment', 'text_comment', 'post_comment', 'confirmation_comment', 'date_comment')
    list_display_links = ('author_comment', 'text_comment', 'confirmation_comment')
    list_filter = ('author_comment', 'text_comment', 'post_comment', 'confirmation_comment', 'date_comment')
    search_fields = ('author_comment', 'post_comment', 'confirmation_comment', 'date_comment')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
