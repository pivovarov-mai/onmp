from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from config.utils import (
    parse_data_to_client,
)

from .utils import (
    get_all_diseases,
    get_diseases_by_tag,
    get_diseases_by_part_of_tag,
)

from .swagger import (
    SW_GET_DISEASES,
    SW_GET_DISEASES_BY_TAG,
    SW_GET_DISEASES_BY_PART_OF_TAG,
)


class GetDiseases(APIView):
    '''
    View to get diseases. Data is caching, so each next attempts will be faster than first one
    '''

    @swagger_auto_schema(**SW_GET_DISEASES)
    def get(self, request):
        current_cache_name = 'diseases_all'
        result = cache.get(current_cache_name)
        if result is None:
            result = parse_data_to_client(get_all_diseases(), 3)
            cache.set(current_cache_name, result, None)
        return Response(result)


class GetDiseasesByTag(APIView):
    '''
    View to get diseases by tag. Data is caching, so each next attempts will be faster than first one
    '''

    @swagger_auto_schema(**SW_GET_DISEASES_BY_TAG)
    def get(self, request):
        tag = request.GET.get('tag', False)
        if tag is False:
            return Response({'error': 'Код не был введен'},
                            status=status.HTTP_418_IM_A_TEAPOT)

        tag_wout_space = tag.replace(' ', '_')
        current_cache_name = f'diagnoses_by_code_{tag_wout_space}'
        result = cache.get(current_cache_name)
        if result is None:
            result = parse_data_to_client(get_diseases_by_tag(tag), 3)
            if result != []:
                cache.set(current_cache_name, result, None)
        return Response(result)


class GetDiseasesByPartOfTag(APIView):
    '''
    View to get diseases by part of tag. Data is caching, so each next attempts will be faster than first one
    '''

    @swagger_auto_schema(**SW_GET_DISEASES_BY_PART_OF_TAG)
    def get(self, request):
        part_of_tag = request.GET.get('part_of_tag', False)
        if part_of_tag is False:
            return Response({'error': 'Часть тэга не была введена'},
                            status=status.HTTP_418_IM_A_TEAPOT)

        part_of_tag_w_space = part_of_tag.replace(' ', '_')
        current_cache_name = f'diseases_by_part_of_tag_{part_of_tag_w_space}'
        result = cache.get(current_cache_name)
        if result is None:
            result = parse_data_to_client(get_diseases_by_part_of_tag(
                part_of_tag), 3)
            if result != []:
                cache.set(current_cache_name, result, 36000)  # 10h
        return Response(result)
