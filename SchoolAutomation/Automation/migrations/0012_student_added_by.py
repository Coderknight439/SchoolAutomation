# Generated by Django 2.1.7 on 2019-04-03 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Automation', '0011_auto_20190328_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='added_by',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
