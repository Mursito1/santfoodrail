from django.urls import path
from blog import views

urlpatterns = [
    path('', views.render_articles, name='index'),
    path('menus', views.menus, name = 'menus'),
    path('registro', views.registro , name = 'registro'),
    path('nosotros', views.nosotros, name = 'nosotros'),
    path('contacto', views.contacto, name = 'contacto'),
    path('login', views.login, name = 'login'),
]