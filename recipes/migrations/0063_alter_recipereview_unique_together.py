# Generated by Django 4.1.5 on 2023-03-03 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0062_rename_reciperating_recipereview'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='recipereview',
            unique_together=set(),
        ),
    ]