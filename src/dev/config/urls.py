from django.contrib import admin
from django.urls import path, include

from .views import StartPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', StartPage.as_view(), name='home'),
]
