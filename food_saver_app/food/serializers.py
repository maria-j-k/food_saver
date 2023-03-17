from rest_framework import serializers

from .choices import FoodCategoryChoices, MeasureChoices

# from .models import Components, Ingredients, Products, Quantities, Recipes
from .models import Products, Quantities
from .utils import get_choices_error_message


class BaseChoicesWriteSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        extra_kwargs = self.get_extra_kwargs()
        self.choice_field = extra_kwargs["choice_field"]
        self.choices = extra_kwargs["choices"]

        self.fields[self.choice_field].error_messages["invalid_choice"] = get_choices_error_message(
            self.choice_field
        )

    def to_internal_value(self, data):
        if isinstance(self.choice_field, str):
            value = data[self.choice_field]
            data[self.choice_field] = self.sanitaze_category(value=value.upper())
        return super().to_internal_value(data)

    def sanitaze_category(self, value):
        try:
            return self.choices[value].value
        except KeyError:
            return value


class ProductReadSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = ["name", "category"]

    def get_category(self, obj: Products) -> str:
        return obj.get_category_display()


class ProductWriteSerializer(BaseChoicesWriteSerializer):
    class Meta:
        model = Products
        fields = ["name", "category"]
        extra_kwargs = {"choice_field": "category", "choices": FoodCategoryChoices}


class QuantityReadSerializer(serializers.ModelSerializer):
    mesure = serializers.SerializerMethodField()

    class Meta:
        model = Quantities
        fields = ["measure", "amount"]

    def get_mesure(self, obj: Quantities):
        return obj.get_mesure_display()


class QuantityWriteSerializer(BaseChoicesWriteSerializer):
    class Meta:
        model = Quantities
        fields = ["measure", "amount"]
        extra_kwargs = {"choice_field": "measure", "choices": MeasureChoices}


# class ComponentWriteSerializer(serializers.ModelSerializer):
#     name = ProductWriteSerializer
#     quantity = QuantityWriteSerializer

#     class Meta:
#         model = Components
#         fields = ["name", "quantity"]


# class IngredientWriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ingredients
#         fields = ["component"]


# class RecipeWriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Recipes
#         fields = ["name", "description", "ingredients", "servings", "type", "private"]


# class Recipes(models.Model):
#     name = models.CharField(max_length=250)
#     description = models.TextField()
#     ingredients = models.ManyToManyField(Ingredients)
#     servings = models.PositiveIntegerField()
#     type = models.IntegerField(choices=TypeChoices.choices)

#     def __str__(self):
#         return self.name
