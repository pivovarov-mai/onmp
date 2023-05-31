from django.urls import path

from .views import (
    GetDiseases,
    GetDiseasesByTag,
    GetDiseasesByPartOfTag,
    # AddDisease,
    ShowAllDiseases,
    GetDiseasesByName,
    GetSimpleDiseases,
)


urlpatterns = [
    path('get_diseases/',
         GetDiseases.as_view(),
         name='get_diseases'),
    path('get_diseases_by_tag/',
         GetDiseasesByTag.as_view(),
         name='get_diseases_by_tag'),
    path('get_diseases_by_part_of_tag/',
         GetDiseasesByPartOfTag.as_view(),
         name='get_diseases_by_part_of_tag'),
    # path('add_disease/',
    #      AddDisease.as_view(),
    #      name='add_disease/'),
    path('show_all_diseases/',
         ShowAllDiseases.as_view(),
         name='show_disease/'),
    path('get_diseases_by_name/',
         GetDiseasesByName.as_view(),
         name='get_diseases_by_name/'),
    path('get_simple_diseases/',
         GetSimpleDiseases.as_view(),
         name='get_simple_diseases/'),
]
