from django import forms
from .models import *


class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = "__all__"


class SubjectForm(forms.ModelForm):
	class Meta:
		model = Subject
		fields = "__all__"


class SectionForm(forms.ModelForm):
	class Meta:
		model = Section
		fields = "__all__"


class ExamForm(forms.ModelForm):
	class Meta:
		model = Exam
		fields = "__all__"


class ClassForm(forms.ModelForm):
	class Meta:
		model = Class
		fields = "__all__"


class DepartmentForm(forms.ModelForm):
	class Meta:
		model = Department
		fields = "__all__"
