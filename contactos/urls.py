from rest_framework import routers
from .views import ContactoViewSet

router = routers.DefaultRouter()
router.register(r'contactos', ContactoViewSet, basename='contacto')

urlpatterns = router.urls