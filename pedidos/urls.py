from rest_framework import routers
from .views import Pedido_MenuViewSet, PedidoViewSet

router = routers.DefaultRouter()
router.register(r'pedido', PedidoViewSet, basename='pedido')
router.register(r'pedido_menu', Pedido_MenuViewSet, basename='pedido_menu')

urlpatterns = router.urls