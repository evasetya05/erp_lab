# Generated by Django 5.2.2 on 2025-06-10 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_media', '0005_blog_ig'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='for_who',
            new_name='for_market',
        ),
        migrations.RenameField(
            model_name='ig',
            old_name='for_who',
            new_name='for_market',
        ),
        migrations.RenameField(
            model_name='linkedin',
            old_name='for_who',
            new_name='for_market',
        ),
    ]
