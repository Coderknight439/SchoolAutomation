
from django.contrib import admin
from .models import Class, Section, Department, Exam, Student, Subject, ResultOfficer

# Register your models here.
admin.site.register(Class)
admin.site.register(Section)
admin.site.register(Department)
admin.site.register(Exam)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(ResultOfficer)
admin.site.site_header = 'Milestone Automation'
admin.site.site_title = 'Milestone Automation'
admin.site.index_title = 'Milestone Automation'
