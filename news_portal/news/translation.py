from .models import Category, Post
from modeltranslation.translator import register, TranslationOptions


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title_category',)


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title_post', 'text_post')
