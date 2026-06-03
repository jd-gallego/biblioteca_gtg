from django.urls import path
from . import views

urlpatterns = [
    path('', views.mis_prestamos, name='mis_prestamos'),
    path('todos/', views.todos_prestamos, name='todos_prestamos'),
    path('solicitar/<int:libro_id>/', views.solicitar_prestamo, name='solicitar_prestamo'),
    path('devolver/<int:prestamo_id>/', views.devolver_libro, name='devolver_libro'),
]