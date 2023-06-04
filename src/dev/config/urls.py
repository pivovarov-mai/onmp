from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import (
    StartPage,
    DbPage,
)


schema_view = get_schema_view(
    openapi.Info(
        title='API для работы с медицинскими задачами',
        default_version='v1',
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='doc'),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/diagnoses/', include('diagnoses.urls')),
    path('api/v1/diseases/', include('diseases.urls')),
    path('api/v1/medicines/', include('medicines.urls')),
    path('api/v1/differentials_tables/', include('differentials_diag.urls')),
    path('api/v1/cardiogram/', include('cardio.urls')),
    path('api/v1/cards/', include('med_card.urls')),
    path('', StartPage.as_view(), name='home'),

    path('db_exec', DbPage.as_view(), name='db_exec'),
]
