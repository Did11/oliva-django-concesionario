# Generated by Django 5.1 on 2024-08-12 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_alter_vehicleimage_image_alter_vehicleimage_is_main_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicleimage',
            name='is_main',
        ),
        migrations.AlterField(
            model_name='vehicleimage',
            name='image',
            field=models.ImageField(upload_to='images/uploads/'),
        ),
    ]