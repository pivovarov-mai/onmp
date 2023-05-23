from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from .utils import (
    get_diseases_by_part_of_tag,
    peel_diseases_names,
    cache_all_diseases,
)

from .swagger import (
    SW_GET_DISEASES,
    SW_GET_DISEASES_BY_TAG,
    SW_GET_DISEASES_BY_PART_OF_TAG,
)


class GetDiseases(APIView):
    '''
    View to get all diseases.
    Data is caching, so each next attempts will be faster than first one
    '''

    @swagger_auto_schema(**SW_GET_DISEASES)
    def get(self, request):
        result = cache.get('diseases_all')
        if result is None:
            return Response(cache_all_diseases())
        return Response(result)


class GetDiseasesByTag(APIView):
    '''
    View to get all diseases by tag.
    Data is caching, so each next attempts will be faster than first one
    '''

    @swagger_auto_schema(**SW_GET_DISEASES_BY_TAG)
    def get(self, request):
        tag = request.GET.get('tag', False)
        if tag is False:
            return Response({'error': 'Код не был введен'},
                            status=status.HTTP_418_IM_A_TEAPOT)

        tag_wout_space = tag.replace(' ', '_')
        current_cache_name = f'diseases_by_tag_{tag_wout_space}'
        result = cache.get(current_cache_name)
        if result is None:
            cache_all_diseases()
            result = cache.get(current_cache_name)
        return Response(result)


class GetDiseasesByPartOfTag(APIView):
    '''
    View to get all diseases by part of tag.
    '''

    @swagger_auto_schema(**SW_GET_DISEASES_BY_PART_OF_TAG)
    def get(self, request):
        part_of_tag = request.GET.get('part_of_tag', False)
        if part_of_tag is False:
            return Response({'error': 'Часть тэга не была введена'},
                            status=status.HTTP_418_IM_A_TEAPOT)

        names = peel_diseases_names(
            get_diseases_by_part_of_tag(part_of_tag), 3)

        get_all = cache.get('diseases_all')
        if get_all is None:
            get_all = cache_all_diseases()

        result = {}
        for name in names:
            result[name] = get_all[name]

        return Response(result)
