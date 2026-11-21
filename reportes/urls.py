from django.urls import path
from . import views

app_name = 'reportes'

urlpatterns = [
    path('', views.indice, name='indice'),
    path('estudiantes/csv/', views.estudiantes_csv, name='estudiantes_csv'),
    path('estudiantes/pdf/', views.estudiantes_imprimir, name='estudiantes_pdf'),
]
