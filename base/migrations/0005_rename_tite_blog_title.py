# Generated by Django 4.0.4 on 2022-05-14 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_title_blog_tite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='tite',
            new_name='title',
        ),
    ]
