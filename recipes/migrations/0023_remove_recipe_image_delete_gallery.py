# Generated by Django 4.1.5 on 2023-01-19 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0022_remove_recipe_image_recipe_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='image',
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
    ]
