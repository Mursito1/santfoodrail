from rest_framework import routers
from .views import PedidoViewSet

router = routers.DefaultRouter()
router.register(r'pedido', PedidoViewSet, basename='pedido')

urlpatterns = router.urls