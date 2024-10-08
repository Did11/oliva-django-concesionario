# Generated by Django 5.1 on 2024-08-11 22:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0003_alter_vehicle_brand_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='vehicles/images/')),
                ('is_main', models.BooleanField(default=False)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='vehicles.vehicle')),
            ],
        ),
    ]
