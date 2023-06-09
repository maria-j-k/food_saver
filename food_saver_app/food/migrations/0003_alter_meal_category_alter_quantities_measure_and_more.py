# Generated by Django 4.1.7 on 2023-03-13 16:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("food", "0002_alter_products_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meal",
            name="category",
            field=models.IntegerField(choices=[(0, "Breakfast"), (1, "Elevenses"), (2, "Lunch"), (4, "Dinner")]),
        ),
        migrations.AlterField(
            model_name="quantities",
            name="measure",
            field=models.IntegerField(
                choices=[
                    (0, "Gram"),
                    (1, "Spoon"),
                    (2, "Teaspoon"),
                    (3, "Cup"),
                    (4, "Pitch"),
                    (5, "Handful"),
                    (6, "Tuft"),
                    (7, "Spring"),
                    (8, "Leaf"),
                    (9, "Piece"),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="recipes",
            name="type",
            field=models.IntegerField(
                choices=[(0, "Soup"), (1, "Main Dish"), (2, "Salat"), (3, "Omlet"), (4, "Fricassee")]
            ),
        ),
        migrations.AlterField(
            model_name="stockmeals",
            name="type",
            field=models.IntegerField(
                choices=[(0, "Soup"), (1, "Main Dish"), (2, "Salat"), (3, "Omlet"), (4, "Fricassee")]
            ),
        ),
    ]
