# Generated by Django 4.1.5 on 2023-01-18 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_alter_ingredients_salt_alter_ingredients_calorie_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredients',
            name='Salt',
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='calorie',
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='fat',
        ),
    ]
