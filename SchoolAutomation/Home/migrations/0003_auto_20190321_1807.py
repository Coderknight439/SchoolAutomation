# Generated by Django 2.1.7 on 2019-03-21 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20190320_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='father_phone',
            field=models.IntegerField(verbose_name='Mobile'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='moher_phone',
            field=models.IntegerField(verbose_name='Mobile'),
        ),
    ]
