# Generated by Django 5.0 on 2024-09-20 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
