from django.urls import path
from .views import (
    CreateListCardAPI,
    RetrieveUpdateDeleteCardAPI,
)


urlpatterns = [
    path('card_jobs/',
         CreateListCardAPI.as_view(),
         name='create_list_card'),
    path('card_jobs/<int:id>/',
         RetrieveUpdateDeleteCardAPI.as_view(),
         name='retrieve_update_delete_card'),
]
