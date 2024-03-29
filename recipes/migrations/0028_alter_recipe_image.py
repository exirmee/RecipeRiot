# Generated by Django 4.1.5 on 2023-01-20 01:30

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0027_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='/recipe_images/default.jpg', force_format=None, help_text='Enter ------', keep_meta=True, null=True, quality=-1, scale=None, size=[100, 150], upload_to='recipe_images/'),
        ),
    ]
