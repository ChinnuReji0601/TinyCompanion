# Generated by Django 5.1.2 on 2024-11-15 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0010_toy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
    ]