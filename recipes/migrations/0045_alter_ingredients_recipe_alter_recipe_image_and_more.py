# Generated by Django 4.1.5 on 2023-02-01 12:44

from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0044_recipecats_rename_parentcategory_parentcats_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='/recipe_images/default.jpg', force_format='WebP', help_text='choose an image for the recipe', keep_meta=True, null=True, quality=80, scale=None, size=[850, 450], upload_to='recipe_images/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='outro',
            field=django_quill.fields.QuillField(help_text='add some notes for the recipe'),
        ),
    ]
