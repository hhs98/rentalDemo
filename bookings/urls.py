from django.urls import path

from .views import BookingViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = router.urls
