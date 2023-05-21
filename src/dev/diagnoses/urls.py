from django.urls import path


from .views import (
    GetDiagnoses,
    GetDiagnosesByCode,
    GetDiagnosesByPartOfCode,
)


urlpatterns = [
    path('get_diagnoses/',
         GetDiagnoses.as_view(),
         name='get_diagnoses'),
    path('get_diagnoses_by_code/',
         GetDiagnosesByCode.as_view(),
         name='get_diagnoses_by_code'),
    path('get_diagnoses_by_part_of_code/',
         GetDiagnosesByPartOfCode.as_view(),
         name='get_diagnoses_by_part_of_code'),
]
