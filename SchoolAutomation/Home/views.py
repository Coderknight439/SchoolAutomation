from django.contrib import messages
from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from .forms import AdmissionForm
from Automation.models import ResultOfficer
from django.views.generic import ListView
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect


# Create your views here.

def resultadmin_required(user):
	if user:
		return user.groups.filter(name='ResultAdmin').count() == 1
	return False


def admin_required(user):
	if user.is_superuser:
		return True
	return False


def index(request):
	"""Renders the home page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'Home/index.html',
		{
			'title': 'Home Page',
			'year': datetime.now().year,
		}
	)


def new_form(request):
	if request.method == "POST":
		form = AdmissionForm(request.POST)
		if form.is_valid():
			post = form.save(commit=True)
			post.save()
			messages.success(request, 'Your Application Submitted Succesfully')
			form = AdmissionForm()
	else:
		form = AdmissionForm()
	return render(request, 'Home/admissionform.html', {'form': form})


class ResultAdminListView(ListView):
	queryset = ResultOfficer.objects.all()


@login_required(login_url='/Automation/login/')
@user_passes_test(admin_required, login_url='/Automation/login')
def createresultadmin(request):
	if request.method == 'POST':
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		phone = request.POST['phone']
		email = request.POST['email']
		address = request.POST['address']
		password = 'milestone123'
		form = ResultAdmin.objects.create(
			first_name=firstname,
			last_name=lastname,
			email=email,
			address=address,
			phone_no=phone,
		)
		user = User.objects.create_user(email, email, password)
		user.save()
		group = Group.objects.get(name='ResultAdmin')
		group.user_set.add(user)
		messages.success(request, 'Result Admin Added Succesfully')
		form.save()
		return redirect('/resultadminlist')
	return render(request, 'Automation/resultadmincreate.html', {'title': 'Create Result Admin'})


@login_required(login_url='/Automation/login/')
@user_passes_test(resultadmin_required, login_url='/Automation/login')
def resultadminprofile(request):
	teacher = ResultOfficer.objects.get(email=request.user)
	user = User.objects.get(username=request.user)
	return render(request, 'Automation/resultadminprofile.html', {'teacher': teacher, 'user': user})
