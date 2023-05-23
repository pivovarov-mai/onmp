from django.urls import path

from .views import (
    GetMedicines,
)


urlpatterns = [
    path('get_medicines/',
         GetMedicines.as_view(),
         name='get_medicines'),
]
