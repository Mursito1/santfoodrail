from rest_framework import routers
from .views import ContactoViewSet, Estado_contactoViewSet, Tipo_contactoViewSet

router = routers.DefaultRouter()
router.register(r'contacto', ContactoViewSet, basename='contacto')

router.register(r'tipo_contacto', Tipo_contactoViewSet, basename='tipo_contacto')

router.register(r'estado_contacto', Estado_contactoViewSet, basename='estado_contacto')

urlpatterns = router.urls