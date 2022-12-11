from rest_framework import viewsets, mixins

from .models import Return

from .serializers import ReturnSerializer


class ReturnViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer
