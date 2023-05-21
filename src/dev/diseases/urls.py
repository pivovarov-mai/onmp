from django.urls import path

from .views import (
    GetDiseases,
    GetDiseasesByTag,
    GetDiseasesByPartOfTag,
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
]
