from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from .utils import (
    get_all_medicines_by_adult_filter,
    get_all_medicines_by_child_filter,
    get_all_medicines_by_part_of_name_by_adult_filter,
    get_all_medicines_by_part_of_name_by_child_filter,

    peel_medicines_by_filters,
)

from .swagger import (
    SW_GET_MEDICINES,
)


class GetMedicines(APIView):
    '''
    View to get medicines.
    Data is caching, so each next attempts will be faster than first one
    '''

    @swagger_auto_schema(**SW_GET_MEDICINES)
    def get(self, request):
        if request.GET.get('search', '') == '':
            cache_take = cache.get('medicines_all')
            if cache_take is None:
                result = peel_medicines_by_filters(
                    get_all_medicines_by_adult_filter(),
                    get_all_medicines_by_child_filter()
                )
                cache.set('medicines_all', result, None)
                return Response(result)
            return Response(cache_take)

        search = request.GET['search']
        return Response(
            peel_medicines_by_filters(
                    get_all_medicines_by_part_of_name_by_adult_filter(search),
                    get_all_medicines_by_part_of_name_by_child_filter(search),
                )
            )
