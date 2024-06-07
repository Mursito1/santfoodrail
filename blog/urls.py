from django.urls import include, path
from blog import views

urlpatterns = [
    path('', views.render_articles, name='index'),
    path('menus', views.menus, name = 'menus'),
    path('registro', views.registro , name = 'registro'),
    path('nosotros', views.nosotros, name = 'nosotros'),
    path('contacto', views.contacto, name = 'contacto'),
    path('login', views.login, name = 'login'),
    path('registro', views.registro, name = 'registro'),
    path('crud', views.crud, name = 'crud'),
    path('pago', views.pago, name = 'pago'),
    path('agregar/<int:menu_id>/', views.agregar_menu, name='Add'),
    path('eliminar/<int:menu_id>/', views.eliminar_menu, name='Del'),
    path('restar/<int:menu_id>/', views.restar_menu, name='Sub'),
    path('limpiar/', views.limpiar_carrito, name='CLS'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('perfil/', views.perfil, name='perfil'),
    path('modificar-producto/<id>/', views.modificar_producto, name='modificar_producto'),
    path('editar_contacto/<int:id>/', views.editar_contacto, name='editar_contacto'),
    path('guardar_pedido/', views.guardar_pedido, name='guardar_pedido'),
    path('revisar_pedidos/', views.revisar_pedidos, name='revisar_pedidos'),
    path('menu/<int:menu_id>/', views.detalle_menu, name='detalle_menu'),
]