from django.contrib import admin
from django.urls import path, include

from .views import (
    StartPage,
    DbPage,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/diagnoses/', include('diagnoses.urls')),
    path('', StartPage.as_view(), name='home'),
    path('db_exec', DbPage.as_view(), name='db_exec'),
]
