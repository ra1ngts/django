from django import template

register = template.Library()

censored_words = ['почувствовала', 'мгновенно']


@register.filter()
def censor(words):
    if str(censored_words):
        for word in censored_words:
            if word in words:
                words = words.replace(word[1:-1], '*' * len(word))
    return words
