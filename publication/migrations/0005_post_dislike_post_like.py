# Generated by Django 4.0 on 2022-01-02 23:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publication', '0004_post_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislike',
            field=models.ManyToManyField(blank=True, related_name='blog_posts_dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='blog_posts_like', to=settings.AUTH_USER_MODEL),
        ),
    ]