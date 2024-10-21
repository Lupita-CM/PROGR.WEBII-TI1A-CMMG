from django.urls import path
from .views import cargar_municipios, index

urlpatterns = [
    path('', index, name='index'),
    path('ajax/cargar-municipios/', cargar_municipios, name='ajax_cargar_municipios'),
]