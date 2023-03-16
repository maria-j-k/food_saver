from rest_framework import serializers

from .choices import FoodCategoryChoices
from .models import Products
from .utils import get_choices_error_message


class ProductReadSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = ["id", "name", "category"]

    def get_category(self, obj: Products) -> str:
        return obj.get_category_display()


class ProductWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ["name", "category"]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["category"].error_messages["invalid_choice"] = get_choices_error_message(
            "category"
        )

    def to_internal_value(self, data):
        category = data["category"]
        if isinstance(category, str):
            data["category"] = self.sanitaze_category(category.upper())
        return super().to_internal_value(data)

    def sanitaze_category(self, value):
        try:
            return FoodCategoryChoices[value].value
        except KeyError:
            return value
