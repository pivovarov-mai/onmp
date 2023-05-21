from drf_yasg import openapi


SW_GET_DISEASES = {
    'responses': {
        '200': openapi.Response(
            description='Выводит все заболевания, внизу представлен один пример',
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


SW_GET_DISEASES_BY_TAG = {
    'manual_parameters': [
        openapi.Parameter(
            'tag',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            required=True
        ),
    ],
    'responses': {
        '200': openapi.Response(
            description='Выводит заболевание или совокупность заболеваний по полному тэгу',
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
        '418': 'tag параметр не обнаружен',
    },
}


SW_GET_DISEASES_BY_PART_OF_TAG = {
    'manual_parameters': [
        openapi.Parameter(
            'part_of_tag',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            required=True
        ),
    ],
    'responses': {
        '200': openapi.Response(
            description='Выводит заболевание или совокупность заболеваний по неполному тэгу',
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
        '418': 'part_of_code параметр не обнаружен',
    },
}
