from django.urls import include, path
from blog import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.render_articles, name='index'),
    path('menus', views.menus, name = 'menus'),
    path('registro', views.registro , name = 'registro'),
    path('nosotros', views.nosotros, name = 'nosotros'),
    path('contacto', views.contacto, name = 'contacto'),
    path('login', views.login, name = 'login'),
    path('registro', views.registro, name = 'registro'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name='password_reset_complete'),
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
    path('agregar-proteina/', views.agregar_proteina, name='agregar_proteina'),
    path('agregar-salsa/', views.agregar_salsa, name='agregar_salsa'),
    path('agregar-vegetal/', views.agregar_vegetal, name='agregar_vegetal'),
    path('ingredientes/', views.lista_ingredientes, name='lista_ingredientes'),
    path('proteina/editar/<int:id>/', views.editar_proteina, name='editar_proteina'),
    path('proteina/eliminar/<int:id>/', views.eliminar_proteina, name='eliminar_proteina'),
    path('vegetal/editar/<int:id>/', views.editar_vegetal, name='editar_vegetal'),
    path('vegetal/eliminar/<int:id>/', views.eliminar_vegetal, name='eliminar_vegetal'),
    path('salsa/editar/<int:id>/', views.editar_salsa, name='editar_salsa'),
    path('salsa/eliminar/<int:id>/', views.eliminar_salsa, name='eliminar_salsa'),
    path('editar-usuario/', views.editar_usuario, name='editar_usuario'),
    

]

    
