# Generated by Django 2.1.7 on 2019-03-16 20:43

import Home.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('Class', models.CharField(choices=[('six', 'VI'), ('nine', 'IX')], default='VI', max_length=100, verbose_name='Sought Admission in')),
                ('medium', models.CharField(choices=[('Bangla', 'Bangla'), ('English', 'English')], default='Bangla', max_length=100, verbose_name='Medium')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='Male', max_length=20, verbose_name='Gender')),
                ('height', models.FloatField(default='5.3', verbose_name='Height')),
                ('weight', models.FloatField(default='45.2', verbose_name='Weight')),
                ('blood', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('O+', 'O+'), ('O-', 'O-')], default='A+', max_length=20, verbose_name='Blood Group')),
                ('dob', models.DateField(default=datetime.date.today, verbose_name='Date of Birth')),
                ('religion', models.CharField(choices=[('islam', 'Islam'), ('hindu', 'Hinduism'), ('buddha', 'Buddhaism'), ('christian', 'Christian'), ('other', 'Other')], default='Islam', max_length=100, verbose_name='Religion')),
                ('father_first_name', models.CharField(max_length=50, verbose_name='Father Name (First)')),
                ('father_last_name', models.CharField(max_length=50, verbose_name='Father Name (Last)')),
                ('fathers_qualification', models.CharField(choices=[('ssc', 'SSC'), ('hsc', 'HSC'), ('honors', 'Honors'), ('masters', 'Masters'), ('others', 'Others')], default='SSC', max_length=100, verbose_name='Fathers (Qualification)')),
                ('father_occupation', models.CharField(max_length=50, verbose_name='Occupation')),
                ('father_phone', models.CharField(max_length=50, verbose_name='Mobile')),
                ('mother_first_name', models.CharField(max_length=50, verbose_name='Mother Name (Frist)')),
                ('mother_last_name', models.CharField(max_length=50, verbose_name='Mother Name (Last)')),
                ('mohers_qualification', models.CharField(choices=[('ssc', 'SSC'), ('hsc', 'HSC'), ('honors', 'Honors'), ('masters', 'Masters'), ('others', 'Others')], default='SSC', max_length=100, verbose_name='Mothers (Qualification)')),
                ('mother_occupation', models.CharField(max_length=50, verbose_name='Occupation')),
                ('moher_phone', models.CharField(max_length=50, verbose_name='Mobile')),
                ('address', models.CharField(default='Uttara', max_length=200, verbose_name='Address')),
                ('last_class', models.CharField(choices=[('six', 'VI'), ('seven', 'VII'), ('eight', 'VIII'), ('nine', 'IX'), ('ten', 'X')], default='VI', max_length=100, verbose_name='Last Class Attended')),
                ('last_school', models.CharField(default='Milestone', max_length=100, verbose_name='Last School')),
                ('session', models.IntegerField(default=Home.models.current_date, verbose_name='Session')),
                ('approved', models.BooleanField(blank='True', default='False')),
            ],
        ),
    ]
