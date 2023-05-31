from drf_yasg import openapi

SW_CARDIO_SEND = {
    'manual_parameters': [
        openapi.Parameter(
            'cardiogram',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_FILE,
            required=True
        ),
    ],
    'responses': {
        '200': openapi.Response(
            description='Топология',
        ),
        '418': 'Файл не передан',
    },
}
