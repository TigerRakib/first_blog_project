# Generated by Django 5.0 on 2024-09-22 07:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
