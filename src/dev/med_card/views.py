from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from config.loggers_conf import slog

from .utils import (
    card_create,
    show_all_cards,
    retrieve_card,
    update_card,
    delete_card,
)

from .swagger import (
    SW_LIST_CARDS,
    SW_CREATE_CARD,
)


class CreateListCardAPI(APIView):
    '''
    View to create or list cards
    '''
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**SW_LIST_CARDS)
    def get(self, request):
        '''
        View to get a list of cards
        '''
        return Response(show_all_cards(request.user.pk))

    @swagger_auto_schema(**SW_CREATE_CARD)
    def post(self, request):
        '''
        View to create new card
        '''
        return Response(card_create({
            'account_user_id': request.user.pk,
            **request.data.dict()})
        )


class RetrieveUpdateDeleteCardAPI(APIView):
    '''
    View to retrieve update delete card with get post delete methods
    '''
    permission_classes = [IsAuthenticated]

    def get(self, request, id, **kwargs):
        '''
        View to retrieve card by id
        '''
        result = retrieve_card(id)
        if result is None:
            return Response('Карта не найдена',
                            status=status.HTTP_404_NOT_FOUND)
        if result['account_user_id'] != request.user.pk:
            return Response('Доступ запрещен',
                            status=status.HTTP_409_CONFLICT)

        if 'down_methods_required' not in kwargs:
            del result['account_user_id']
        return Response(result)

    def put(self, request, id):
        '''
        View to update card by id
        '''
        card = self.get(request, id, down_methods_required=True)

        if card.status_code == 200:
            card = card.data
            if card['account_user_id'] != request.user.pk:
                return Response('Доступ недоступен',
                                status=status.HTTP_409_CONFLICT)

            inputs = request.data.dict()
            for field in card:
                if field in inputs:
                    card[field] = inputs[field]
            try:
                update_card(card)
                return Response('Данные обновлены')
            except Exception as e:
                slog(str(e))
                return Response('Ошибка, проверьте логи')
        else:
            return Response(card.data)

    def delete(self, request, id):
        '''
        View to delete card by id
        '''
        card = self.get(request, id, down_methods_required=True)

        if card.status_code == 200:
            card = card.data
            if card['account_user_id'] != request.user.pk:
                return Response('Доступ недоступен',
                                status=status.HTTP_409_CONFLICT)

            try:
                delete_card(id)
                return Response('Карта удалена')
            except Exception as e:
                slog(str(e))
                return Response('Ошибка, проверьте логи')
        else:
            return Response(card.data)
