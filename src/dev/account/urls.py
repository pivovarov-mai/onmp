from django.urls import path
from django.contrib.auth.views import LogoutView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import (
    LoginView,              # Low level
    RegisterView,           # Low level
    
    UserGetTokenAPI,
    UserCreateAPI,
    GetProfileAPI,
    CheckEmailAPI,
)

schema_view = get_schema_view(
    openapi.Info(
        title='API для управления аккаунтами',
        default_version='v1',
    ),
    public=False,
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('token/', UserGetTokenAPI.as_view(), name='token'),
    path('user_create/', UserCreateAPI.as_view(), name='user_create'),
    path('user_profile/', GetProfileAPI.as_view(), name='user_profile'),
    path('email_confirm/<uuid:id>', CheckEmailAPI.as_view(), name='email_confirm'),
    
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='account_swagger'),
]
