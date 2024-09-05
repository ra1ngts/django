from django.shortcuts import render


def e_handler403(request, exception):
    context = {'title': 'Ошибка доступа: 403',
               'error_message': 'Доступ к этой странице ограничен',
               }
    return render(request, 'utils/403.html', status=403, context=context)


def e_handler404(request, exception):
    context = {'title': 'Страница не найдена: 404',
               'error_message': 'К сожалению такая страница была не найдена, или перемещена',
               }
    return render(request, 'utils/404.html', status=404, context=context)


def e_handler500(request):
    context = {'title': 'Ошибка сервера: 500',
               'error_message': 'Внутренняя ошибка сайта, вернитесь на главную страницу,'
                                ' отчет об ошибке мы направим администрации сайта',
               }
    return render(request, 'utils/500.html', status=500, context=context)
