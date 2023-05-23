from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from .utils import (
    get_all_diags,
    get_all_diags_by_name,
)

from .swagger import (
    SW_GET_DIAGS,
)


class GetAllDiags(APIView):
    '''
    View to get all diff tables.
    If name is not defined returns all data
    Data is caching, so each next attempts will be faster than first one
    '''

    @swagger_auto_schema(**SW_GET_DIAGS)
    def get(self, request):
        if 'name' in request.GET:
            return Response(get_all_diags_by_name(request.GET['name']))
        return Response(get_all_diags())
