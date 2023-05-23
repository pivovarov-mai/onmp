from django.urls import path

from .views import (
    GetAllDiags,
)


urlpatterns = [
    path('get_diff_tables/', GetAllDiags.as_view(), name='get_diags'),
]
