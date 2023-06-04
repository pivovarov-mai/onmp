from django.urls import path
from .views import CardiogramSend


urlpatterns = [
    path('cardiogram_send/', CardiogramSend.as_view(), name='cardiogram_send'),
]
