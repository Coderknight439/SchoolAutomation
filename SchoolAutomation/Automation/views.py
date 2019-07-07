from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib import messages
from .models import *
from Home.models import Admission
from Home.forms import AdmissionForm, ApproveForm
from .forms import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	CreateView,
	ListView
)


# Create your views here.

class admin(UserPassesTestMixin):

	def test_func(self):
		return self.request.user.is_superuser


def admin_required(user):
	if user.is_superuser:
		return True
	return False


def resultadmin_required(user):
	if user:
		return user.groups.filter(name='ResultAdmin').count() == 1
	return False


def Principal_required(user):
	if user:
		return user.groups.filter(name='Principal').count() == 1
	return False


def AdmissionOfficer_required(user):
	if user:
		return user.groups.filter(name='AdmissionOfficer').count() == 1
	return False


def Teacher_required(user):
	if user:
		return user.groups.filter(name='Teacher').count() == 1
	return False


def Student_required(user):
	if user:
		return user.groups.filter(name='Student').count() == 1
	return False


def index(request):
	"""Renders the home page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'Automation/index.html',
		{
			'year': datetime.now().year,
			'title': 'Milestone Automation'
		}
	)


@login_required(login_url='/Automation/login/')
@user_passes_test(Student_required, login_url='/Automation/login')
def studenthome(request):
	"""Renders the home page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'Automation/studenthome.html',
		{
			'year': datetime.now().year,
			'title': 'Student Home'
		}
	)


@login_required(login_url='/Automation/index/')
@user_passes_test(Teacher_required, login_url='/Automation/login')
def teacherthome(request):
	"""Renders the home page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'Automation/teacherhome.html',
		{
			'year': datetime.now().year,
			'title': 'Teacher Home'
		}
	)


@login_required(login_url='/Automation/index')
@user_passes_test(Principal_required, login_url='/Automation/login')
def principalhome(request):
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'Automation/principalhome.html',
		{
			'year': datetime.now().year,
			'test': Admission.objects.filter(approved=False, session=datetime.now().year),
			'title': 'Principal Home'
		}
	)


@login_required(login_url='/Automation/login')
@user_passes_test(admin_required, login_url='/Automation/login')
def adminhome(request):
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'Automation/adminhome.html',
		{
			'year': datetime.now().year,
			# 'test': Admission.objects.filter(approved=False, session=datetime.now().year),
			'title': 'Admin Home'
		}
	)


@login_required(login_url='/Automation/index/')
@user_passes_test(AdmissionOfficer_required, login_url='/Automation/login')
def applicantlist(request):
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'Automation/applicantlist.html',
		{
			'year': datetime.now().year,
			'test': Admission.objects.filter(approved=True, is_student=False, session=datetime.now().year),
			'title': 'Applicant List'
		}
	)


@login_required(login_url='/Automation/index/')
@user_passes_test(AdmissionOfficer_required, login_url='/Automation/login')
def admissionhome(request):
	"""Renders the home page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'Automation/admission.html',
		{
			'year': datetime.now().year,
			'title': 'Admission Home'
		}
	)


@login_required(login_url='/Automation/index/')
@user_passes_test(resultadmin_required, login_url='/Automation/login')
def resultadmin(request):
	"""Renders the home page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'Automation/resultadmin.html',
		{
			'year': datetime.now().year,
			'title': 'Result Admin Home'
		}
	)


@login_required(login_url='/Automation/index/')
@user_passes_test(Principal_required, login_url='/Automation/login')
def approveform(request, pk):
	if pk:
		form = Admission.objects.get(pk=pk)
		p = Admission.objects.get(pk=pk)
		form = ApproveForm(instance=form)
		if request.method == 'POST':
			Admission.objects.filter(pk=pk, approved=False).update(approved=True)
			messages.success(request, 'Applicant Approved Succesfully')
			return redirect('/Automation/principalhome')
		else:
			return render(request, 'Automation/formapprove.html', {'year': datetime.now().year, 'form': form, 'test': p, 'title': 'Applicant Approve'})


@login_required(login_url='/Automation/index/')
@user_passes_test(Principal_required, login_url='/Automation/login')
def deleteform(request, pk):
	if pk:
		obj = get_object_or_404(Admission, pk=pk)
	if request.method == 'POST':
		obj.delete()
		messages.success(request, "Applicant deleted succesfully")
		return redirect('/Automation/principalhome')

	context = {
		'object': obj,
		'title': 'Delete Applicant'
	}
	return render(request, 'Automation/confirmdelete.html', context)


@login_required(login_url='/Automation/login/')
@user_passes_test(AdmissionOfficer_required, login_url='/Automation/login')
def createstudent(request, pk):
	todo = Admission.objects.get(pk=pk)
	Class = todo.Class
	FormID = todo.id
	sec = Section.objects.all()
	test = Student.objects.latest('pk')
	x = int(test.UserID) + 1
	UserID = str(x)
	if request.method == 'POST':
		# UserID = request.POST['UserID']
		# Password = request.POST['Password']
		section = request.POST['section']
		usermail = UserID + '@milestone.edu'
		student = Student.objects.create(
			FormID=FormID,
			Class=Class,
			UserID=x,
			section=section,
			added_by=str(request.user)
		)
		Admission.objects.filter(pk=pk, is_student=False).update(is_student=True)
		user = User.objects.create_user(UserID, usermail, 'milestone123')
		user.save()
		group = Group.objects.get(name='Student')
		group.user_set.add(user)
		messages.success(request, 'Student Approved Succesfully')
		student.save()
		return redirect('/Automation/applicantlist')
	else:
		form = StudentForm()
	return render(request, 'Automation/Studentcreate.html',
				  {'form': form, 'UserID': UserID, 'title': 'Create Student', 'sec': sec})


def user_login(request):
	context = {'title': 'Login'}
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			if user.groups.filter(name='Student'):
				return redirect('/Automation/studenthome')
			elif user.groups.filter(name='Principal'):
				return redirect('/Automation/principalhome')
			elif user.groups.filter(name='Teacher'):
				return redirect('/Automation/teacherhome')
			elif user.groups.filter(name='AdmissionOfficer'):
				return redirect('/Automation/admissionhome')
			elif user.groups.filter(name='ResultAdmin'):
				return redirect('/Automation/resultadmin')
			elif user.is_superuser:
				return redirect('/Automation/adminhome')
			else:
				context['error'] = 'Provide Valid Credentials'
				return render(request, 'Automation/login.html', context)
		else:
			context['error'] = 'Provide Valid Credentials'
			return render(request, 'Automation/login.html', context)
	else:
		return render(request, 'Automation/login.html', context)


def user_logout(request):
	logout(request)
	return redirect('/Automation/index')


@login_required(login_url='/Automation/login/')
@user_passes_test(resultadmin_required, login_url='/Automation/login')
def addresult(request):
	ex = Exam.objects.all()
	subject = Subject.objects.all()
	sec = Section.objects.all()
	cls = Class.objects.all()
	if request.method == 'POST':
		Class1 = request.POST['Class']
		section = request.POST['section']
		exam = request.POST['exam']
		subject = request.POST['subject']
		request.session['exam'] = exam
		request.session['subject'] = subject
		request.session['class'] = Class1
		request.session['section'] = section
		student = Student.objects.filter(Class=Class1, section=section)
		return render(
			request,
			'Automation/mark.html',
			{'student': student, 'year': datetime.now().year, 'Class': Class, 'section': section, 'subject': subject})
	return render(request, 'Automation/addresult.html', {'title': 'Add Result', 'exam': ex, 'subject': subject, 'sec': sec, 'Class': cls})


@login_required(login_url='/Automation/index/')
@user_passes_test(resultadmin_required, login_url='/Automation/login')
def mark(request):
	exam = request.session['exam']
	subject = request.session['subject']
	Class = request.session['class']
	section = request.session['section']
	if request.method == 'POST':
		n = Student.objects.filter(Class=Class, section=section).count()
		i = 1
		while i <= n:
			studentid = request.POST['studentid' + str(i)]
			mark = request.POST['mark' + str(i)]
			post = result.objects.create(
				studentid=studentid,
				examid=exam,
				subjectid=subject,
				mark=mark,
				year=datetime.now().year,
				added_by=str(request.user)
			)
			post.save()
			i += 1
		messages.success(request, 'Result Added Succesfully')
		return redirect('/Automation/addresult')
	return render(request, 'Automation/mark.html', {'title': 'Add Mark'})


@login_required(login_url='/Automation/index/')
@user_passes_test(Student_required, login_url='/Automation/login')
def studentprofile(request):
	student = Student.objects.get(UserID=request.user)
	user = User.objects.get(username=request.user)
	formid = student.FormID
	form = Admission.objects.get(id=formid)
	return render(request, 'Automation/studentprofile.html', {'forms': form, 'student': student, 'user': user})


@login_required(login_url='/Automation/index/')
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			return redirect('/Automation/password')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'accounts/change_password.html', {'form': form, 'title': 'Password Change'})


@login_required(login_url='/Automation/index/')
@user_passes_test(Student_required, login_url='/Automation/login')
def view_result(request):
	exam = Exam.objects.all()
	if request.method == 'POST':
		examid = request.POST['examid']
		year = request.POST['year']
		m = result.objects.filter(studentid=request.user, examid=examid, year=year)
		return render(request, 'Automation/showmark.html', {'result': m, 'year': year})
	return render(request, 'Automation/viewresult.html', {'title': 'My Result', 'test': exam})


class ClassListView(LoginRequiredMixin, admin, ListView):
	login_url = '/Automation/login'
	queryset = Class.objects.all()


class SectionListView(LoginRequiredMixin, admin, ListView):
	login_url = '/Automation/login'
	queryset = Section.objects.all()


class ExamListView(LoginRequiredMixin, admin, ListView):
	login_url = '/Automation/login'
	queryset = Exam.objects.all()


class DepartmentListView(LoginRequiredMixin, admin, ListView):
	login_url = '/Automation/login'
	queryset = Department.objects.all()


class SubjectListView(LoginRequiredMixin, admin, ListView):
	login_url = '/Automation/login'
	queryset = Subject.objects.all()


class ClassCreateView(LoginRequiredMixin, admin, CreateView):
	login_url = '/Automation/login'
	template_name = 'Automation/Class_create.html'
	form_class = ClassForm
	queryset = Class.objects.all()

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)


class ExamCreateView(LoginRequiredMixin, admin, CreateView):
	login_url = '/Automation/login'
	template_name = 'Automation/Class_create.html'
	form_class = ExamForm
	queryset = Class.objects.all()

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)


class SectionCreateView(LoginRequiredMixin, admin, CreateView):
	login_url = '/Automation/login'
	template_name = 'Automation/Class_create.html'
	form_class = SectionForm
	queryset = Class.objects.all()

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)


class SubjectCreateView(LoginRequiredMixin, admin, CreateView):
	login_url = '/Automation/login'
	template_name = 'Automation/Class_create.html'
	form_class = SubjectForm
	queryset = Class.objects.all()

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)


class DepartmentCreateView(LoginRequiredMixin, admin, CreateView):
	login_url = '/Automation/login'
	template_name = 'Automation/Class_create.html'
	form_class = DepartmentForm
	queryset = Department.objects.all()

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)


class TeacherListView(LoginRequiredMixin, admin, ListView):
	login_url = '/Automation/login'
	queryset = Teacher.objects.all()


class AdmissionOfficerListView(LoginRequiredMixin, admin, ListView):
	login_url = '/Automation/login'
	queryset = AdmissionOfficer.objects.all()


''' @login_required(login_url='/Automation/login/')
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
		return redirect('/Automation/resultadminlist')
	return render(request, 'Automation/resultadmincreate.html', {'title': 'Create Result Admin'}) '''


@login_required(login_url='/Automation/login/')
@user_passes_test(admin_required, login_url='/Automation/login')
def createadmissionofficer(request):
	if request.method == 'POST':
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		phone = request.POST['phone']
		email = request.POST['email']
		address = request.POST['address']
		password = 'milestone123'
		form = AdmissionOfficer.objects.create(
			first_name=firstname,
			last_name=lastname,
			email=email,
			address=address,
			phone_no=phone,
		)
		user = User.objects.create_user(email, email, password)
		user.save()
		group = Group.objects.get(name='AdmissionOfficer')
		group.user_set.add(user)
		messages.success(request, 'Admission Officer Added Succesfully')
		form.save()
		return redirect('/Automation/admissionofficerlist')

	return render(request, 'Automation/admissionofficercreate.html', {'title': 'Create Admission Officer'})


@login_required(login_url='/Automation/login/')
@user_passes_test(admin_required, login_url='/Automation/login')
def createteacher(request):
	dept = Department.objects.all()
	if request.method == 'POST':
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		phone = request.POST['phone']
		department = request.POST['department']
		email = request.POST['email']
		address = request.POST['address']
		password = 'milestone123'
		form = Teacher.objects.create(
			first_name=firstname,
			last_name=lastname,
			email=email,
			address=address,
			phone_no=phone,
			department=department,
		)
		user = User.objects.create_user(email, email, password)
		user.save()
		group = Group.objects.get(name='Teacher')
		group.user_set.add(user)
		messages.success(request, 'Teacher Added Succesfully')
		form.save()
		return redirect('/Automation/teacherlist')

	return render(request, 'Automation/teachercreate.html', {'title': 'Create Admission Officer', 'dept': dept})


@login_required(login_url='/Automation/index/')
@user_passes_test(Teacher_required, login_url='/Automation/login')
def teacherprofile(request):
	teacher = Teacher.objects.get(email=request.user)
	depid = teacher.department
	dept = Department.objects.get(id=depid)
	department = dept.departmentname
	user = User.objects.get(username=request.user)
	# formid = student.FormID
	# form = Admission.objects.get(id=formid)
	return render(request, 'Automation/teacherprofile.html', {'teacher': teacher, 'user': user, 'Dept': department})


def passwordsuccess(request):
	test = request.user
	if test is not None:
		login(request, test)
		if test.groups.filter(name='Student'):
			return redirect('/Automation/studenthome')
		elif test.groups.filter(name='Principal'):
			return redirect('/Automation/principalhome')
		elif test.groups.filter(name='Teacher'):
			return redirect('/Automation/teacherhome')
		elif test.groups.filter(name='AdmissionOfficer'):
			return redirect('/Automation/admissionhome')
		elif test.groups.filter(name='ResultAdmin'):
			return redirect('/Automation/resultadmin')
		elif test.is_superuser:
			return redirect('/Automation/adminhome')
		else:
			return render(request, 'Automation/login.html')
	else:
		return render(request, 'Automation/login.html')


@login_required(login_url='/Automation/login/')
@user_passes_test(AdmissionOfficer_required, login_url='/Automation/login')
def admissionofficerprofile(request):
	teacher = AdmissionOfficer.objects.get(email=request.user)
	user = User.objects.get(username=request.user)
	return render(request, 'Automation/admissionofficerprofile.html', {'teacher': teacher, 'user': user})
