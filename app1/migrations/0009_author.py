# Generated by Django 5.0 on 2024-09-19 08:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=100)),
                ('joined_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
