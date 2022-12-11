from rest_framework import routers

from .views import ReturnViewSet

router = routers.SimpleRouter()
router.register(r'returns', ReturnViewSet, basename='return')

urlpatterns = router.urls

