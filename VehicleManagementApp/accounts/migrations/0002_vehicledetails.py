# Generated by Django 4.1.3 on 2022-11-02 16:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VehicleNumber', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator])),
                ('VehicleType', models.CharField(choices=[('TwoWheeler', 'TwoWheeler'), ('ThreeWheeler', 'ThreeWheeler'), ('FourWheeler', 'FourWheeler')], max_length=20)),
                ('VehicleModel', models.CharField(max_length=60)),
                ('VehicleDescription', models.CharField(max_length=300)),
            ],
        ),
    ]
