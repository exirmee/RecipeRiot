# Generated by Django 4.1.5 on 2023-01-26 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0035_rename_user_profile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
