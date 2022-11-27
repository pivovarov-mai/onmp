from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    LoginView,              # Low level
    RegisterView,           # Low level
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', RegisterView.as_view(), name='signup'),
]
