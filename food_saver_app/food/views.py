from rest_framework import viewsets

from .models import Products, Quantities
from .serializers import (
    ProductReadSerializer,
    ProductWriteSerializer,
    QuantityReadSerializer,
    QuantityWriteSerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProductReadSerializer
        return ProductWriteSerializer


class QuantityViewSet(viewsets.ModelViewSet):
    queryset = Quantities.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return QuantityReadSerializer
        return QuantityWriteSerializer
