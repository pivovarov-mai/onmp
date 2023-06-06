from drf_yasg import openapi


SW_GET_DIAGS = {
    'manual_parameters': [
        openapi.Parameter(
            'name',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
        ),
        openapi.Parameter(
            'age',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
        ),
    ],
    'responses': {
        '200': openapi.Response(
            description='Выводит диагностические таблицы - пример формата ниже',
            examples={
                'application/json': {
                    "Шкала оценки вероятности ТЭЛА (Revised Geneva Score)": {
                        "data": {
                            "Шкала оценки вероятности ТЭЛА (Revised Geneva Score)": [
                                {
                                    "Признак": "Возраст старше 65 лет",
                                    "Баллы": "+1"
                                },
                                {
                                    "Признак": "Кровохарканье",
                                    "Баллы": "+2"
                                }
                            ],
                            "Интерпретация результата": [
                                {
                                    "Клиническая вероятность": "Низкая",
                                    "Сумма баллов": 0
                                },
                                {
                                    "Клиническая вероятность": "Низкая",
                                    "Сумма баллов": 1
                                }
                            ]
                        },
                        "part_name": "Шкала оценки вероятности ТЭЛА",
                        "note": "",
                        "type_table": 3,
                        "type_result": 5
                    },
                    "Акушерство": {
                        "data": [
                            {
                                "Срок": "12 недель",
                                "ВДМ": "2-6",
                                "ОЖ": None
                            },
                            {
                                "Срок": "16 недель",
                                "ВДМ": "10-18",
                                "ОЖ": None
                            },
                        ],
                        "part_name": "",
                        "note": "",
                        "type_table": 1,
                        "type_result": 1
                    }
                }
            }
        ),
    },
}
