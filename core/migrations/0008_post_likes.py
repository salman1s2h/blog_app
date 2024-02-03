# Generated by Django 4.2.9 on 2024-01-22 14:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_remove_like_post_remove_like_user_like_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blog_post_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
