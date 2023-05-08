from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import (
    GetDiagnose,
)

schema_view = get_schema_view(
    openapi.Info(
        title='API для работы с заболеваниями',
        default_version='v1',
    ),
    public=True,
)

urlpatterns = [
    path('get_diagnose/', GetDiagnose.as_view(), name='get_diagnose'),
    path('doc/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='diagnose_swagger'),
]
