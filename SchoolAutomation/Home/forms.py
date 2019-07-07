
from django import forms
from .models import Admission


class AdmissionForm(forms.ModelForm):

	class Meta:
		model = Admission
		fields = "__all__"
		exclude = ['approved', 'session', 'is_student']


class ApproveForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	Class = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	medium = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	gender = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	religion = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	father_first_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	father_last_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	fathers_qualification = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	father_occupation = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	father_phone = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	mother_first_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	mother_last_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	mothers_qualification = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	mother_occupation = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	moher_phone = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	last_class = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	last_school = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

	class Meta:
		model = Admission
		fields = "__all__"
		exclude = ['blood', 'height', 'weight', 'dob', 'address', 'session', 'is_student']
