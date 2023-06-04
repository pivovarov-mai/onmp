from django.urls import path

from .views import (
    CreateListTemplatesView,
    RetrieveUpdateDeleteTemplateView,
    GeneratePDFAPI,
    AttachMedicineAPI,
)


urlpatterns = [
    path('template_jobs/',
         CreateListTemplatesView.as_view(),
         name='create_list_template'),
    path('template_jobs/<int:id>/',
         RetrieveUpdateDeleteTemplateView.as_view(),
         name='retrieve_update_delete_template'),
    path('generate_pdf/<int:id>/',
         GeneratePDFAPI.as_view(),
         name='generate_pdf'),
    path('medicine_attach/<int:id>/',
         AttachMedicineAPI.as_view(),
         name='template_medicine_attach'),
]
