# Generated by Django 5.0.6 on 2024-06-16 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_car_picture_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]