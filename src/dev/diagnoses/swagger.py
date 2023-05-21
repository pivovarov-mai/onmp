from drf_yasg import openapi


SW_GET_DIAGNOSES = {
    'responses': {
        '200': openapi.Response(
            description='Выводит все диагнозы, внизу представлен один пример',
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


SW_GET_DIAGNOSES_BY_CODE = {
    'manual_parameters': [
        openapi.Parameter(
            'code',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            required=True
        ),
    ],
    'responses': {
        '200': openapi.Response(
            description='Выводит диагноз или совокупность диагнозов',
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
        '418': 'code параметр не обнаружен',
    },
}


SW_GET_DIAGNOSES_BY_PART_OF_CODE = {
    'manual_parameters': [
        openapi.Parameter(
            'part_of_code',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            required=True
        ),
    ],
    'responses': {
        '200': openapi.Response(
            description='Выводит диагноз или совокупность диагнозов',
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
