# Generated by Django 5.1.2 on 2024-11-18 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0012_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='expiry_date',
            field=models.CharField(max_length=5),
        ),
    ]
