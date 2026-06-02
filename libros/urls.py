from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo_libros, name='catalogo_libros'),
    path('agregar/', views.agregar_libro, name='agregar_libro'),
]