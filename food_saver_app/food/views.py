from rest_framework import viewsets

from .models import Products
from .serializers import ProductReadSerializer, ProductWriteSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProductReadSerializer
        return ProductWriteSerializer
