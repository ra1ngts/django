from django.contrib import admin

from news.models import Author, Category, Post, PostCategory, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_user', 'rating_user')
    list_display_links = ('author_user', 'rating_user')
    search_fields = ('author_user',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title_category',)
    list_display_links = ('title_category',)
    list_filter = ('subscribers',)
    search_fields = ('title_category',)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title_post', 'text_post', 'author_post', 'choice_post', 'date_post', 'rating_post')
    list_display_links = ('title_post', 'author_post', 'choice_post', 'date_post', 'rating_post')
    list_filter = ('author_post', 'choice_post', 'date_post')
    search_fields = ('title_post', 'author_post', 'choice_post', 'date_post', 'rating_post')


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('post_category', 'category_post')
    list_display_links = ('post_category', 'category_post')
    list_filter = ('category_post',)
    search_fields = ('post_category', 'category_post')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post_comment', 'user_comment', 'text_comment', 'date_comment', 'rating_comment')
    list_display_links = ('post_comment', 'user_comment', 'text_comment', 'date_comment', 'rating_comment')
    list_filter = ('user_comment', 'date_comment', 'rating_comment')
    search_fields = ('post_comment', 'user_comment', 'text_comment', 'date_comment', 'rating_comment')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
