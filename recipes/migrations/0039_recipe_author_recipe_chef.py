# Generated by Django 4.1.5 on 2023-01-27 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0038_remove_follow_followed_remove_follow_follower_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(default=1, help_text='Enter ------', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recipe',
            name='chef',
            field=models.CharField(default='new chef', help_text='Enter ------', max_length=100),
        ),
    ]
