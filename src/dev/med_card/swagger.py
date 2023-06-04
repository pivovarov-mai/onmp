from drf_yasg import openapi


SW_LIST_CARDS = {
    'manual_parameters': [
        openapi.Parameter('token',
                            in_=openapi.IN_HEADER,
                            type=openapi.TYPE_STRING,
                            required=True),
    ],
    'responses': {
        '200': 'Вывод всех карт пользователя',
        '4+': 'Ошибка будет указана в ответе'
    }
}


SW_CREATE_CARD = {
    'manual_parameters': [
        openapi.Parameter('token',
                            in_=openapi.IN_HEADER,
                            type=openapi.TYPE_STRING,
                            required=True),
        openapi.Parameter('name',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING,
                            required=True),
        openapi.Parameter('order',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING,
                            required=True),
        openapi.Parameter('date',
                            in_=openapi.IN_QUERY,
                            description='Формат YYYY-MM-DD',
                            type=openapi.TYPE_STRING),
        openapi.Parameter('status',
                            in_=openapi.IN_QUERY,
                            description='Один из: "draft", "ready", "archive", "template" (черновик, завершена, архивная, шаблон). Если не указать, то по дефолту - "draft"',
                            type=openapi.TYPE_STRING),
        openapi.Parameter('comment',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING),
    ],
    'responses': {
        '200': 'Вывод всех карт пользователя',
        '4+': 'Ошибка будет указана в ответе'
    }
}
