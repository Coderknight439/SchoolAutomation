
from django.db import models
import datetime
from django.urls import reverse

# Create your models here.
Gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
BLOOD_GROUP = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B-', 'B-'),
    ('AB-', 'AB-'),
    ('AB+', 'AB+'),
    ('O+', 'O+'),
    ('O-', 'O-'),
)
Medium = (
    ('Bangla', 'Bangla'),
    ('English', 'English'),
)
CLASS = (
    ('Six', 'VI'),
    ('Seven', 'VII'),
    ('Eight', 'VIII'),
    ('Nine', 'IX'),
    ('Ten', 'X'),
)
SOUGHT_CLASS = (
    ('Six', 'VI'),
    ('Seven', 'VII'),
    ('Eight', 'VIII'),
    ('Nine', 'IX'),
    ('Ten', 'X'),
)
RELIGION = (
    ('Islam', 'Islam'),
    ('Hindu', 'Hinduism'),
    ('Buddha', 'Buddhaism'),
    ('Christian', 'Christian'),
    ('Other', 'Other')
)
QUALIFICATION = (
    ('SSC', 'SSC'),
    ('HSC', 'HSC'),
    ('Honors', 'Honors'),
    ('Masters', 'Masters'),
    ('Others', 'Others'),
)


def current_date():
    return datetime.date.today().year


class Admission(models.Model):

    first_name = models.CharField(max_length=50, blank=False, verbose_name='First Name')
    last_name = models.CharField(max_length=50, blank=False, verbose_name='Last Name')
    Class = models.CharField(default='VI', choices=SOUGHT_CLASS, blank=False,
                             max_length=100, verbose_name='Sought Admission in')
    medium = models.CharField(default='Bangla', choices=Medium, blank=False,
                              max_length=100, verbose_name='Medium')
    gender = models.CharField(default='Male', choices=Gender,
                              max_length=20, blank=False, verbose_name='Gender')
    height = models.FloatField(
        default='5.3', blank=False, verbose_name='Height')
    weight = models.FloatField(
        default='45.2', blank=False, verbose_name='Weight')
    blood = models.CharField(default='A+', max_length=20, choices=BLOOD_GROUP,
                             blank=False, verbose_name='Blood Group')
    dob = models.DateField(blank=False,  # default=datetime.date.today,
                           verbose_name='Date of Birth')
    religion = models.CharField(default='Islam', choices=RELIGION, blank=False,
                                max_length=100, verbose_name='Religion')
    father_first_name = models.CharField(
        max_length=50, blank=False, verbose_name='Father Name (First)')
    father_last_name = models.CharField(
        max_length=50, blank=False, verbose_name='Father Name (Last)')
    fathers_qualification = models.CharField(default='SSC',
                                             choices=QUALIFICATION, blank=False, max_length=100, verbose_name='Fathers (Qualification)')
    father_occupation = models.CharField(max_length=50, blank=False, verbose_name='Occupation')
    father_phone = models.IntegerField(blank=False, verbose_name='Mobile')
    mother_first_name = models.CharField(
        max_length=50, blank=False, verbose_name='Mother Name (Frist)')
    mother_last_name = models.CharField(
        max_length=50, blank=False, verbose_name='Mother Name (Last)')
    mothers_qualification = models.CharField(default='SSC',
                                            choices=QUALIFICATION, blank=False, max_length=100, verbose_name='Mothers (Qualification)')
    mother_occupation = models.CharField(max_length=50, blank=False, verbose_name='Occupation')
    moher_phone = models.IntegerField(blank=False, verbose_name='Mobile')
    address = models.CharField(default='Uttara', max_length=200,
                               blank=False, verbose_name='Address')
    last_class = models.CharField(default='VI', choices=CLASS, max_length=100,
                                  blank=False, verbose_name='Last Class Attended')
    last_school = models.CharField(default='Milestone', blank=False,
                                   max_length=100, verbose_name='Last School')
    session = models.IntegerField(default=current_date, verbose_name='Session')
    approved = models.BooleanField(default='False', blank='True')
    is_student = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.first_name

