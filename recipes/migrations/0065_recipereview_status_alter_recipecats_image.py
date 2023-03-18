# Generated by Django 4.1.5 on 2023-03-04 20:55

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0064_recipereview_image_recipereview_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipereview',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('approved', 'Approved'), ('denied', 'Denied')], default='draft', max_length=10),
        ),
        migrations.AlterField(
            model_name='recipecats',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='/cats/default.jpg', force_format='WebP', keep_meta=True, null=True, quality=80, scale=None, size=[430, 290], upload_to='cats_images/'),
        ),
    ]
