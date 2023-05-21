from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from config.utils import (
    parse_data_to_client,
)

from .utils import (
    get_all_medicines,
    get_medicines_by_name,
    get_medicines_by_part_of_name,

    peel_medicines,
)

from .swagger import (
    SW_GET_MEDICINES,
    SW_GET_MEDICINES_BY_PART_OF_NAME,
    SW_GET_MEDICINES_BY_NAME
)


class GetMedicines(APIView):
    '''
    View to get medicines. Data is caching, so each next attempts will be faster than first one
    '''

    @swagger_auto_schema(**SW_GET_MEDICINES)
    def get(self, request):
        if request.GET.get('search', '') == '':
            # cache_take = cache.get('medicines_all')
            cache_take = None
            if cache_take is None:
                result = peel_medicines(get_all_medicines())
                cache.set('medicines_all', result, None)
                return Response(result)
            return Response(cache_take)

        return Response(
            peel_medicines(
                get_medicines_by_part_of_name(
                        request.GET['search']
                    )
                )
            )


class GetMedicinesByName(APIView):
    '''
    View to get medicines by name. Data is caching, so each next attempts will be faster than first one
    '''

    @swagger_auto_schema(**SW_GET_MEDICINES_BY_NAME)
    def get(self, request):
        name = request.GET.get('name', False)
        if name is False:
            return Response({'error': 'Имя не было введено'},
                            status=status.HTTP_418_IM_A_TEAPOT)

        name_wout_space = name.replace(' ', '_')
        current_cache_name = f'medicines_by_name_{name_wout_space}'
        result = cache.get(current_cache_name)
        if result is None:
            result = parse_data_to_client(get_medicines_by_name(name))
            if result != []:
                cache.set(current_cache_name, result, None)
        return Response(result)


class GetMedicinesByPartOfName(APIView):
    '''
    View to get medicines by part of name. Data is caching, so each next attempts will be faster than first one
    '''

    @swagger_auto_schema(**SW_GET_MEDICINES_BY_PART_OF_NAME)
    def get(self, request):
        part_of_name = request.GET.get('part_of_name', False)
        if part_of_name is False:
            return Response({'error': 'Часть тэга не была введена'},
                            status=status.HTTP_418_IM_A_TEAPOT)

        part_of_tag_w_space = part_of_name.replace(' ', '_')
        current_cache_name = f'diseases_by_part_of_tag_{part_of_tag_w_space}'
        result = cache.get(current_cache_name)
        if result is None:
            result = parse_data_to_client(get_medicines_by_part_of_name(
                part_of_name))
            if result != []:
                cache.set(current_cache_name, result, 36000)  # 10h
        return Response(result)
