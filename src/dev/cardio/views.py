import random

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from .swagger import SW_CARDIO_SEND


class CardiogramSend(APIView):
    '''
    View to send cardiogram and get info about rough topology.
    Do not use swagger, use curl instead.
    '''

    @swagger_auto_schema(**SW_CARDIO_SEND)
    def post(self, request):
        if 'cardiogram' not in request.FILES:
            return Response("Необходим файл в переменную 'cardiogram'",
                            status=status.HTTP_418_IM_A_TEAPOT)

        image = request.FILES['cardiogram']
        file_name = str(random.randint(0, 100)) + '.png'
        default_storage.save(file_name,
                             ContentFile(image.read()))

        return Response('Фотография будет обработана и выслан результат')
