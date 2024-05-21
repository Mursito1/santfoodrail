# calificaciones/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('menu/<int:id_menu>/', views.detalle_menu, name='detalle_menu'),
]
