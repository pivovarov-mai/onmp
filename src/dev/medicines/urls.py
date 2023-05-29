from django.urls import path

from .views import (
    GetMedicines,
    ShowAllMedicines,
)


urlpatterns = [
    path('get_medicines/',
         GetMedicines.as_view(),
         name='get_medicines'),
    path('show_all_medicines/',
         ShowAllMedicines.as_view(),
         name='show_all_medicines'),
]
