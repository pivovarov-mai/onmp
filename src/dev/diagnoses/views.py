from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from django.core.cache import cache

from .utils import (
    get_all_separated_diagnoses_by_part_of_code,
    cache_diagnoses,
    peel_diagnoses,
    show_all_diagnoses,
)

from .swagger import (
    SW_GET_DIAGNOSES,
    SW_GET_DIAGNOSES_BY_CODE,
    SW_GET_DIAGNOSES_BY_PART_OF_CODE,
    SW_SHOW_ALL_DIAGNOSES,
)


class GetDiagnoses(APIView):
    '''
    View to get diagnoses.
    Data is caching, so each next attempts will be faster than first one
    '''

    @swagger_auto_schema(**SW_GET_DIAGNOSES)
    def get(self, request):
        cache_result = cache.get('diagnoses_all')
        if cache_result is None:
            return Response(cache_diagnoses())
        return Response(cache_result)


class GetDiagnosesByCode(APIView):
    '''
    View to get diagnoses by code.
    Data is caching, so each next attempts will be faster than first one
    '''

    @swagger_auto_schema(**SW_GET_DIAGNOSES_BY_CODE)
    def get(self, request):
        code = request.GET.get('code', False)
        if code is False:
            return Response({'error': 'Код не был введен'},
                            status=status.HTTP_418_IM_A_TEAPOT)

        get_all = cache.get('diagnoses_all')
        if get_all is None:
            cache_diagnoses()
            get_all = cache.get('diagnoses_all')

        return Response(get_all[code])


class GetDiagnosesByPartOfCode(APIView):
    '''
    View to get diagnoses by part of code.
    '''

    @swagger_auto_schema(**SW_GET_DIAGNOSES_BY_PART_OF_CODE)
    def get(self, request):
        part_of_code = request.GET.get('part_of_code', False)
        if part_of_code is False:
            return Response({'error': 'Часть кода не была введена'},
                            status=status.HTTP_418_IM_A_TEAPOT)

        get_all_result = \
            get_all_separated_diagnoses_by_part_of_code(part_of_code)
        return Response(peel_diagnoses(
            get_all_result[0],
            get_all_result[1]))


class ShowAllDiagnoses(APIView):
    '''
    View to return simple json diagnoses, just diagnose's names in a list.
    Doesn't caching. Doesn't required admin permissions.
    '''

    @swagger_auto_schema(**SW_SHOW_ALL_DIAGNOSES)
    def get(self, request):
        need_to_parse = show_all_diagnoses()
        result = set()
        for item in need_to_parse:
            for diagnose in need_to_parse[item]:
                result.add(diagnose)
        return Response(sorted(result))
