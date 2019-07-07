from django.conf.urls import url
from .views import *
from django.shortcuts import redirect

urlpatterns = [
	url(r'^$', index, name='Home/index'),
	url(r'^index', index, name='Home/index'),
	url(r'^admin', lambda _: redirect('admin:index'), name='Home/admin'),
	url(r'AdmissionForm', new_form, name='Home/admissionform'),
	url(r'^resultadminlist', ResultAdminListView.as_view(), name='Automation/resultadminlist'),
	url(r'^resultadmincreate', createresultadmin, name='Automation/createresultadmin'),
	url(r'^resultadminprofile', resultadminprofile, name='Automation/resultadminprofile'),
]
