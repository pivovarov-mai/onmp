from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

MSG = 'Это мираж, будет добавлено, как администратор будет под этиловым спиртом'


class CreateListTemplatesView(APIView):
    '''
    View to create or list templates
    '''
    permission_classes = [IsAuthenticated]

    def get(self, request):
        '''
        View to list all user's templates
        '''
        return Response(MSG)

    def post(self, request):
        '''
        View to create new template
        '''
        return Response(MSG)


class RetrieveUpdateDeleteTemplateView(APIView):
    '''
    View to retrieve update or delete template
    '''
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        '''
        View to retrieve template by id
        '''
        return Response(MSG)

    def put(self, request, id):
        '''
        View to update existing template by id
        '''
        return Response(MSG)

    def delete(self, request, id):
        '''
        View to delete existing template by id
        '''
        return Response(MSG)


class GeneratePDFAPI(APIView):
    '''
    View to send existing template to pdf generator and get uri address
    '''
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        return Response('Ну типо ссылка на скачивание через nginx')


class AttachMedicineAPI(APIView):
    '''
    View to attach existing medicine to existing template
    '''
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response('Ну типо перекидываем препарат в карту, лол')
