# Generated by Django 4.0.4 on 2022-06-06 13:35

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='featured',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
        migrations.AlterField(
            model_name='itemimg',
            name='itemImage',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]