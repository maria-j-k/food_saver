from django.db import models

from .choices import (
    FoodCategoryChoices,
    MealCategoryChoices,
    MeasureChoices,
    TypeChoices,
)


class Quantities(models.Model):
    measure = models.IntegerField(choices=MeasureChoices.choices)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.amount} {self.measure}"


class Products(models.Model):
    name = models.CharField(max_length=250)
    category = models.IntegerField(choices=FoodCategoryChoices.choices)

    def __str__(self):
        return self.name


class Components(models.Model):
    name = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Quantities, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["name", "quantity"]

    def __str__(self):
        return f"{self.name}: {self.quantity}"


class Ingredients(models.Model):
    component = models.ManyToManyField(Components)


class Recipes(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredients)
    servings = models.PositiveIntegerField()
    type = models.IntegerField(choices=TypeChoices.choices)

    def __str__(self):
        return self.name


class Meal(models.Model):
    category = models.IntegerField(choices=MealCategoryChoices.choices)
    recipes = models.ManyToManyField(Recipes)

    def __str__(self):
        return super().__str__()
        # return f"{self.category}: {self.recipes}"  # TODO parse recipes


class StockProducts(models.Model):
    product = models.OneToOneField(Products, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Quantities, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}: {self.quantity}"


class StockMeals(models.Model):
    recipe = models.OneToOneField(Recipes, on_delete=models.CASCADE)
    type = models.IntegerField(choices=TypeChoices.choices)
    prepared = models.DateTimeField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.recipe
