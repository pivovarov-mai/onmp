from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from django.core.cache import cache

from config.utils import parse_data_to_client

from .utils import (
    get_all_diagnoses,
    get_diagnose_by_code,
    get_diagnose_by_part_code,
)

from .swagger import (
    SW_GET_DIAGNOSES,
    SW_GET_DIAGNOSES_BY_CODE,
    SW_GET_DIAGNOSES_BY_PART_OF_CODE,
)


class GetDiagnoses(APIView):
    '''
    View to get diagnoses. Data is caching, so each next attempts will be faster than first one
    '''

    @swagger_auto_schema(**SW_GET_DIAGNOSES)
    def get(self, request):
        current_cache_name = 'diagnoses_all'
        result = cache.get(current_cache_name)
        if result is None:
            result = parse_data_to_client(get_all_diagnoses(), 5)
            cache.set(current_cache_name, result, None)
        return Response(result)


class GetDiagnosesByCode(APIView):
    '''
    View to get diagnoses by code. Data is caching, so each next attempts will be faster than first one
    '''

    @swagger_auto_schema(**SW_GET_DIAGNOSES_BY_CODE)
    def get(self, request):
        code = request.GET.get('code', False)
        if code is False:
            return Response({'error': 'Код не был введен'},
                            status=status.HTTP_418_IM_A_TEAPOT)

        current_cache_name = f'diagnoses_by_code_{code}'
        result = cache.get(current_cache_name)
        if result is None:
            result = parse_data_to_client(get_diagnose_by_code(code), 5)
            if result != []:
                cache.set(current_cache_name, result, None)
        return Response(result)


class GetDiagnosesByPartOfCode(APIView):
    '''
    View to get diagnoses by part of code. Data is caching, so each next attempts will be faster than first one
    '''

    @swagger_auto_schema(**SW_GET_DIAGNOSES_BY_PART_OF_CODE)
    def get(self, request):
        part_of_code = request.GET.get('part_of_code', False)
        if part_of_code is False:
            return Response({'error': 'Часть кода не была введена'},
                            status=status.HTTP_418_IM_A_TEAPOT)

        current_cache_name = f'diagnoses_by_part_of_code_{part_of_code}'
        result = cache.get(current_cache_name)
        if result is None:
            result = parse_data_to_client(get_diagnose_by_part_code(
                part_of_code), 5)
            if result != []:
                cache.set(current_cache_name, result, 36000)  # 10h
        return Response(result)
