from rest_framework import routers
from .views import Ingrediente_menuViewSet, IngredienteViewSet, MenuViewSet

router = routers.DefaultRouter()
router.register(r'menu', MenuViewSet, basename='menu')
router.register(r'ingrediente', IngredienteViewSet, basename='ingrediente')
router.register(r'ingrediente_menu', Ingrediente_menuViewSet, basename='ingrediente_menu')

urlpatterns = router.urls