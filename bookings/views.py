from rest_framework import generics, viewsets, mixins
from .serializers import BookingSerializer
from .models import Booking


class BookingViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
