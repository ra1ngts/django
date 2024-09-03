from modeltranslation.translator import register, TranslationOptions

from main.models import About, Category


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)
