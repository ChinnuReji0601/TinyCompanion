# Generated by Django 5.1.2 on 2024-11-14 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0003_kitten'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='kitten',
            name='breed',
        ),
    ]
