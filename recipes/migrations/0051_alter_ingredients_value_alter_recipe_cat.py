# Generated by Django 4.1.5 on 2023-02-04 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0050_remove_recipe_steps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='value',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cat',
            field=models.ManyToManyField(blank=True, help_text='Select categories for recipe (hold ctrl to select more than one recipe)', null=True, to='recipes.recipecats'),
        ),
    ]
