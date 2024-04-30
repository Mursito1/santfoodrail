from rest_framework import routers
from .views import ContactoViewSet, Estado_contactoViewSet, Tipo_contactoViewSet

router = routers.DefaultRouter()
router.register(r'contacto', ContactoViewSet, basename='contacto')

urlpatterns = router.urls