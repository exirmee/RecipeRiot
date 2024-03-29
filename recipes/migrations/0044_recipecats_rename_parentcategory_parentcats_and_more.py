# Generated by Django 4.1.5 on 2023-01-31 16:47

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0043_alter_ingredients_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeCats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(null=True)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='/recipe_images/default.jpg', force_format='WebP', help_text='Enter ------', keep_meta=True, null=True, quality=80, scale=None, size=[850, 310], upload_to='recipe_images/')),
            ],
            options={
                'verbose_name_plural': 'recipe categories',
            },
        ),
        migrations.RenameModel(
            old_name='ParentCategory',
            new_name='ParentCats',
        ),
        migrations.DeleteModel(
            name='RecipeCategory',
        ),
        migrations.AddField(
            model_name='recipecats',
            name='parent_categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.parentcats'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cat',
            field=models.ManyToManyField(help_text='Select categories for recipe (hold ctrl to select more than one recipe)', to='recipes.recipecats'),
        ),
    ]
