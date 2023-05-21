from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


class GetAllDiags(APIView):
    '''
    View to get all diagnosis tables. Data is caching, so each next attempts will be faster than first one
    '''

    def get(self, request):
        return Response({'test'})
