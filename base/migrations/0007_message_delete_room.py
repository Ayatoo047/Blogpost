# Generated by Django 4.0.4 on 2022-05-18 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateField(auto_now=True)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.blog')),
            ],
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]