from django.db import models


class FoodCategoryChoices(models.IntegerChoices):
    LOOSE = 0
    CANNED = 1
    DAIRY = 2
    VEGETABLES = 3
    FRUITS = 4


class MeasureChoices(models.IntegerChoices):
    GRAM = 0
    SPOON = 1
    TEASPOON = 2
    CUP = 3
    PITCH = 4
    HANDFUL = 5
    TUFT = 6
    SPRING = 7
    LEAF = 8
    PIECE = 9


class TypeChoices(models.IntegerChoices):
    SOUP = 0
    MAIN_DISH = 1
    SALAT = 2
    OMLET = 3
    FRICASSEE = 4


class MealCategoryChoices(models.IntegerChoices):
    BREAKFAST = 0
    ELEVENSES = 1
    LUNCH = 2
    DINNER = 4