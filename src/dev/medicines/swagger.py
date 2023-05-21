from drf_yasg import openapi


SW_GET_MEDICINES = {
    'manual_parameters': [
        openapi.Parameter(
            'search',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
        ),
    ],
    'responses': {
        '200': openapi.Response(
            description='Выводит все препараты, внизу представлен один пример',
            examples={
                'application/json': {
                    "name": "I10-I15.2",
                    "name_diagnosis": "Гипертоническая болезнь (вне криза)",
                    "recommendations": "Рекомендаций нет",
                    "name_tactics": "1. Рекомендовать обратиться в поликлинику.",
                    "name_sub_diagnosis": "При повышении САД не более чем на 20 мм. рт. ст. от привычного",
                    "name_omp": "Не требует антигипертензивной терапии  на этапе оказания неотложной медицинской помощи"
                }
            }
        ),
    },
}


SW_GET_MEDICINES_BY_NAME = {
    'manual_parameters': [
        openapi.Parameter(
            'name',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            required=True
        ),
    ],
    'responses': {
        '200': openapi.Response(
            description='Выводит препараты или совокупность препаратов по полному названию',
            examples={
                'application/json': {
                    "name": "I10-I15.2",
                    "name_diagnosis": "Гипертоническая болезнь (вне криза)",
                    "recommendations": "Рекомендаций нет",
                    "name_tactics": "1. Рекомендовать обратиться в поликлинику.",
                    "name_sub_diagnosis": "При повышении САД не более чем на 20 мм. рт. ст. от привычного",
                    "name_omp": "Не требует антигипертензивной терапии  на этапе оказания неотложной медицинской помощи"
                }
            }
        ),
        '418': 'name параметр не обнаружен',
    },
}


SW_GET_MEDICINES_BY_PART_OF_NAME = {
    'manual_parameters': [
        openapi.Parameter(
            'part_of_name',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            required=True
        ),
    ],
    'responses': {
        '200': openapi.Response(
            description='Выводит препараты или совокупность препаратов по неполному названию',
            examples={
                'application/json': {
                    "name": "I10-I15.2",
                    "name_diagnosis": "Гипертоническая болезнь (вне криза)",
                    "recommendations": "Рекомендаций нет",
                    "name_tactics": "1. Рекомендовать обратиться в поликлинику.",
                    "name_sub_diagnosis": "При повышении САД не более чем на 20 мм. рт. ст. от привычного",
                    "name_omp": "Не требует антигипертензивной терапии  на этапе оказания неотложной медицинской помощи"
                }
            }
        ),
        '418': 'part_of_name параметр не обнаружен',
    },
}
