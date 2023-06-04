from drf_yasg import openapi

SW_GET_TOKEN = {
    'manual_parameters': [
        openapi.Parameter(
            'email',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            required=True
        ),
        openapi.Parameter(
            'password',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            required=True
        ),
    ],
    'responses': {
        '200': openapi.Response(
            description='Параметры вывода',
            examples={
                'application/json': {
                    'token': '932c47474b7c9bdbfb2ad334d9b7b508824c0851',
                }
            }
        ),
        '4+': 'Не авторизован по параметрам, либо не подтвержден email',
    },
}

SW_CREATE_USER = {
    'manual_parameters': [
        openapi.Parameter('email',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING,
                            required=True),
        openapi.Parameter('password',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING,
                            required=True),
        openapi.Parameter('first_name',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING,
                            required=True),
        openapi.Parameter('last_name',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING,
                            required=True),
        openapi.Parameter('middle_name',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING,
                            required=True),
        openapi.Parameter('phone_number',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING),
        openapi.Parameter('passport',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING),
        openapi.Parameter('date_of_birth',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING),
    ],
    'responses': {'201': 'Успешно создан новый аккаунт',
                '4+': 'Ошибка, которая вернется в ответе'}
}

SW_GET_PROFILE = {
    'manual_parameters': [
        openapi.Parameter('token',
                            in_=openapi.IN_HEADER,
                            type=openapi.TYPE_STRING,
                            required=True),
    ],
    'responses': { # fields = ('email', 'first_name', 'last_name', 'is_email_confirmed')
        '200': openapi.Response(
            description='Параметры вывода',
            examples={
                'application/json': {
                    'email': 'admin@admin.ru',
                    'first_name': 'admin',
                    'last_name': 'admin',
                    'is_email_confirmed': 'true',
                }
            }
        ),
        '4+': 'Ошибка будет указана в ответе'
    }
}

SW_SET_PASSWORD = {
    'manual_parameters': [
        openapi.Parameter('token',
                            in_=openapi.IN_HEADER,
                            type=openapi.TYPE_STRING,
                            required=True),
        openapi.Parameter('new password',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING,
                            required=True),
    ],
    'responses': { # fields = ('email', 'first_name', 'last_name', 'is_email_confirmed')
        '200': 'Успех',
        '4+': 'Ошибка будет указана в ответе'
    }
}

SW_RESET_PASSWORD_REQUEST = {
    'manual_parameters': [
        openapi.Parameter('email',
                          in_=openapi.IN_QUERY,
                          type=openapi.TYPE_STRING,
                          required=True)
    ],
    'responses': {
        '200': 'Подтверждение выслано на почту',
        '4+': 'Ошибка в ответе, либо нет такой почты, либо нет вообще параметра'
    }
}

SW_RESET_PASSWORD_CONFIRMATION = {
    'responses': {
        '401': 'Пользователь не найден',
        '200': 'Пароль выслан на почту'
    }
}


SW_RESEND_MAIL = {
    'manual_parameters': [
        openapi.Parameter('email',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING,
                            required=True),
    ],
    'responses': {'201': 'Отправлено сообщение',
                '4+': 'Ошибка, которая вернется в ответе'}
}


SW_SHOW_ALL_PROFILES = {
    'manual_parameters': [
        openapi.Parameter('token',
                            in_=openapi.IN_HEADER,
                            type=openapi.TYPE_STRING,
                            required=True),
    ],
    'responses': {
        '200': 'Выведутся все профили пользователей',
        '4+': 'Ошибка будет указана в ответе'
    }
}


SW_UPDATE_PROFILE = {
    'manual_parameters': [
        openapi.Parameter('token',
                            in_=openapi.IN_HEADER,
                            type=openapi.TYPE_STRING,
                            required=True),
        openapi.Parameter('first_name',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING),
        openapi.Parameter('last_name',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING),
        openapi.Parameter('middle_name',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING),
        openapi.Parameter('phone_number',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING),
        openapi.Parameter('passport',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING),
        openapi.Parameter('date_of_birth',
                            in_=openapi.IN_QUERY,
                            type=openapi.TYPE_STRING),
    ],
    'responses': {
        '200': 'Простое текстовое сообщение успеха',
        '4+': 'Ошибка будет указана в ответе'
    }
}
