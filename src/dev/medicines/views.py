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
    get_cached,
)

from .swagger import (
    SW_GET_MEDICINES,
    SW_SHOW_ALL_MEDICINES,
)


class GetMedicines(APIView):
    '''
    View to get medicines.
    Data is caching, so each next attempts will be faster than first one
    '''

    @swagger_auto_schema(**SW_GET_MEDICINES)
    def get(self, request):
        if request.GET.get('search', '') == '':
            return Response(get_cached())

        search = request.GET['search']
        return Response(
            peel_medicines_by_filters(
                    get_all_medicines_by_part_of_name_by_adult_filter(search),
                    get_all_medicines_by_part_of_name_by_child_filter(search),
                )
            )


class ShowAllMedicines(APIView):
    '''
    View to return simple json medicines, just medicine's names in a list.
    Doesn't caching. Doesn't required admin permissions.
    '''

    @swagger_auto_schema(**SW_SHOW_ALL_MEDICINES)
    def get(self, request):
        return Response(sorted({medicine for medicine in get_cached()}))
