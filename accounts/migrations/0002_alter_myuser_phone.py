# Generated by Django 4.0.4 on 2022-05-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.CharField(blank=True, default='0000000000', max_length=10),
        ),
    ]
