# Generated by Django 5.1 on 2024-08-12 01:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('vehicles', '0003_alter_vehicle_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='vehicles.vehicle'),
        ),
    ]
