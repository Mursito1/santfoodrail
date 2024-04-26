from rest_framework import routers
from .views import ClienteViewSet

router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet, basename='cliente')

urlpatterns = router.urls