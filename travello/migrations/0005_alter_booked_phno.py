# Generated by Django 4.2.1 on 2023-07-18 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_booked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booked',
            name='phno',
            field=models.BigIntegerField(),
        ),
    ]
