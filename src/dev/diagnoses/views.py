from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import get_diagnose_by_field


class GetDiagnose(APIView):
    '''
    View to get diagnose by code name or something else
    '''

    def get(self, request):
        '''
        Pass diagnose's code in get request to get diagnose with this code
        '''
        code = request.GET.get('field', '')
        result = get_diagnose_by_field(code)
        return Response({'result': result})
