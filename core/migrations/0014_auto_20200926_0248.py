# Generated by Django 2.2 on 2020-09-26 02:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20200926_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='expiration',
            field=models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('(0[1-9]|10|11|12)/20[0-9]{2}$')]),
        ),
    ]
