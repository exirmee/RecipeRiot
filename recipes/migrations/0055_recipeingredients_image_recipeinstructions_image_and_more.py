# Generated by Django 4.1.5 on 2023-02-08 21:17

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0054_alter_recipeingredients_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredients',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='/ingredient_images/default.jpg', force_format='WebP', keep_meta=True, null=True, quality=80, scale=None, size=[850, 310], upload_to='ingredient_images/'),
        ),
        migrations.AddField(
            model_name='recipeinstructions',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='/instructions_images/default.jpg', force_format='WebP', keep_meta=True, null=True, quality=80, scale=None, size=[850, 310], upload_to='instructions_images/'),
        ),
        migrations.AddField(
            model_name='recipeinstructions',
            name='order',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(blank=True, help_text='Select ingredients for recipe (hold ctrl to select more than one recipe)', to='recipes.recipeingredients'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.ManyToManyField(blank=True, help_text='Select instructions for recipe (hold ctrl to select more than one recipe)', to='recipes.recipeinstructions'),
        ),
        migrations.AlterField(
            model_name='recipecats',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='/recipe_images/default.jpg', force_format='WebP', keep_meta=True, null=True, quality=80, scale=None, size=[850, 310], upload_to='recipe_images/'),
        ),
    ]
