# Generated by Django 4.1.5 on 2023-02-08 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0057_alter_recipe_difficulty_alter_recipe_timetoprepare'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='intro',
            field=models.TextField(blank=True, help_text='an introduction for the recipe', null=True),
        ),
    ]
