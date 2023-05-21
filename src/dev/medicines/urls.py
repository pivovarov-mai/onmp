from django.urls import path

from .views import (
    GetMedicines,
    GetMedicinesByName,
    GetMedicinesByPartOfName,
)


urlpatterns = [
    path('get_medicines/',
         GetMedicines.as_view(),
         name='get_medicines'),
    # path('get_medicines_by_name/',
    #      GetMedicinesByName.as_view(),
    #      name='get_medicines_by_name'),
    # path('get_medicines_by_part_of_name/',
    #      GetMedicinesByPartOfName.as_view(),
    #      name='get_medicines_by_part_of_name'),
]
