from django import template

register = template.Library()

censored_words = ['показал', 'Входящая', 'состав', 'смазочных']  # Чтобы не писать список плохих слов, для проверки.


@register.filter()
def censor(words):
    try:
        if str(censored_words):
            for word in censored_words:
                if word in words:
                    words = words.replace(word[1:], '*' * len(word))
        return words
    except TypeError:
        raise 'Ошибка: неверный тип данных'
