from rest_framework import serializers

from .models import Products


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = ["name", "category"]

    def get_category(self, obj: Products) -> str:
        return obj.get_category_display()
