from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from .utils import (
    get_diseases_by_part_of_tag,
    get_diseases_by_name,
    peel_diseases_names,
    cache_all_diseases,
    get_cached_diseases,
    peel_diseases,
)

from .swagger import (
    SW_GET_DISEASES,
    SW_GET_DISEASES_BY_TAG,
    SW_GET_DISEASES_BY_PART_OF_TAG,
    SW_SHOW_ALL_DISEASES,
    SW_GET_ALL_DISEASES_BY_NAME,
    SW_GET_ALL_SIMPLE_DISEASE,
)


class GetDiseases(APIView):
    '''
    View to get all diseases.
    Data is caching, so each next attempts will be faster than first one
    '''

    @swagger_auto_schema(**SW_GET_DISEASES)
    def get(self, request):
        return Response(get_cached_diseases())


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

        get_all = get_cached_diseases()

        result = {}
        for name in names:
            result[name] = get_all[name]

        return Response(result)


class GetDiseasesByName(APIView):
    '''
    View to get all diseases by full name.
    Doesn't caching. Doesn't required admin permissions.
    '''

    @swagger_auto_schema(**SW_GET_ALL_DISEASES_BY_NAME)
    def get(self, request):
        name = request.GET.get('name', False)
        if name is False:
            return Response({'error': 'Название не было введено'},
                            status=status.HTTP_418_IM_A_TEAPOT)

        names = peel_diseases(
            get_diseases_by_name(name), 3)
        return Response(names)


class GetSimpleDiseases(APIView):
    '''
    View to get all diseases with only one attribute - tag.
    Doesn't caching. Doesn't required admin permissions.
    '''

    @swagger_auto_schema(**SW_GET_ALL_SIMPLE_DISEASE)
    def get(self, request):
        result = {}
        diseases_all = get_cached_diseases()
        for item in diseases_all:
            result[item] = diseases_all[item]['tag']
        return Response(result)


class ShowAllDiseases(APIView):
    '''
    View to return simple json diseases, just disease's names in a list.
    Doesn't caching. Doesn't required admin permissions.
    '''

    @swagger_auto_schema(**SW_SHOW_ALL_DISEASES)
    def get(self, request):
        return Response(sorted({name for name in get_cached_diseases()}))
