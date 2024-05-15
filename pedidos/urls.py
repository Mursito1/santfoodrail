from rest_framework import routers
from .views import Pedido_menuViewSet, PedidoViewSet

router = routers.DefaultRouter()
router.register(r'pedido', PedidoViewSet, basename='pedido')
router.register(r'pedido_menu', Pedido_menuViewSet, basename='pedido_menu')

urlpatterns = router.urls