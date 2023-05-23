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
                    "S. Amiodaronum 50 mg/ml": {
                        "genitive": "S. Amiodaroni 50 mg/ml",
                        "unit": "mg",
                        "diagnoses": {
                            "Продолжающийся пароксизм фибрилляции предссердий": {
                                "adult_dosage": 300,
                                "child_dosage": None,
                            },
                            "Сохраненяющаяся крупноволновая фибрилляция желудочков или желудочковая тахикардия без пульса": {
                                "adult_dosage": 300,
                                "child_dosage": None,
                            }
                        },
                        "contraindications": ["Синусовая брадикардия",
                                              "СССУ",
                                              "Синоатриальная блокада",
                                              "AV-блокада II-III степени (без использования кардиостимулятора)",
                                              "Кардиогенный шок"],
                        "child_dosage_unit": "weight"
                    }
                }
            }
        ),
    },
}
