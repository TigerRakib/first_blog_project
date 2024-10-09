# Generated by Django 5.0 on 2024-09-14 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_frequently_asked'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('action_time', models.DateTimeField()),
                ('is_error', models.BooleanField(default=False)),
                ('is_success', models.BooleanField(default=False)),
                ('error_message', models.TextField()),
            ],
        ),
    ]
