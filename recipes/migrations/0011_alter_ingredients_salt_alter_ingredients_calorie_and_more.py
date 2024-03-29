# Generated by Django 4.1.5 on 2023-01-18 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_ingredients_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='Salt',
            field=models.DecimalField(decimal_places=3, max_digits=20),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='calorie',
            field=models.DecimalField(decimal_places=3, max_digits=20),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='fat',
            field=models.DecimalField(decimal_places=3, max_digits=20),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='unit',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=20),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='value',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=20),
        ),
    ]
