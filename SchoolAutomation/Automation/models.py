
from django.db import models
from django.urls import reverse
import datetime


# Create your models here.
def current_date():
	return datetime.date.today().year


class Class(models.Model):
	classname = models.CharField(max_length=50, blank=False, verbose_name='Class Name')

	def get_absolute_url(self):
		return reverse("Automation:Automation/classlist")

	def __str__(self):
		return self.classname


class Section(models.Model):
	secname = models.CharField(max_length=20, blank=False, verbose_name='Section Name')

	def get_absolute_url(self):
		return reverse("Automation:Automation/sectionlist")

	def __str__(self):
		return self.secname


class Department(models.Model):
	departmentname = models.CharField(max_length=20, blank=False, verbose_name='Department Name')

	def get_absolute_url(self):
		return reverse("Automation:Automation/departmentlist")

	def __str__(self):
		return self.departmentname


class Exam(models.Model):
	exam_type = models.CharField(max_length=50, blank=False, verbose_name='Exam type')

	def get_absolute_url(self):
		return reverse("Automation:Automation/examlist")

	def __str__(self):
		return self.exam_type


class Student(models.Model):
	FormID = models.CharField(max_length=50, blank=False)
	UserID = models.CharField(max_length=30, blank=False, unique=True, verbose_name='UserID')
	Class = models.CharField(max_length=10, blank=False)
	section = models.CharField(max_length=2, blank=False, verbose_name='Section')
	image = models.ImageField(blank=True, upload_to='media/studentprofile')
	added_by = models.CharField(blank=True, max_length=50)


class result(models.Model):
	studentid = models.CharField(max_length=20, blank=False, verbose_name='Student ID')
	subjectid = models.CharField(max_length=15, blank=False, verbose_name='Subject Code')
	examid = models.CharField(max_length=15, blank=False, verbose_name='Exam Type')
	mark = models.DecimalField(max_digits=4, decimal_places=2, blank=False, verbose_name='Mark')
	year = models.IntegerField(default=current_date)
	added_by = models.CharField(max_length=50, blank=False)


class Subject(models.Model):
	subcode = models.CharField(max_length=10, unique=True, blank=False, verbose_name='Subject Code')
	name = models.CharField(max_length=50, verbose_name='Subject Name')

	def get_absolute_url(self):
		return reverse("Automation:Automation/subjectlist")

	def __str__(self):
		return self.name


class ResultOfficer(models.Model):
	first_name = models.CharField(blank=False, max_length=40, verbose_name='First Name')
	last_name = models.CharField(blank=False, max_length=40, verbose_name='Last Name')
	phone_no = models.IntegerField(blank=False, verbose_name='Phone No')
	email = models.EmailField(blank=False, max_length=40, verbose_name='Email')
	address = models.CharField(blank=False, max_length=40, verbose_name='Address')


class Teacher(models.Model):
	first_name = models.CharField(blank=False, max_length=40, verbose_name='First Name')
	last_name = models.CharField(blank=False, max_length=40, verbose_name='Last Name')
	department = models.CharField(blank=False, max_length=60, verbose_name='Department')
	phone_no = models.IntegerField(blank=False, verbose_name='Phone No')
	email = models.EmailField(blank=False, max_length=40, verbose_name='Email')
	address = models.CharField(blank=False, max_length=40, verbose_name='Address')


class AdmissionOfficer(models.Model):
	first_name = models.CharField(blank=False, max_length=40, verbose_name='First Name')
	last_name = models.CharField(blank=False, max_length=40, verbose_name='Last Name')
	phone_no = models.IntegerField(blank=False, verbose_name='Phone No')
	email = models.EmailField(blank=False, max_length=40, verbose_name='Email')
	address = models.CharField(blank=False, max_length=40, verbose_name='Address')

class Meta:
	ordering = id
