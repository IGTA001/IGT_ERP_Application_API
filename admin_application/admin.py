from django.contrib import admin
from .models import Course,Student
# Register your models here.

admin.site.register(Course.Course)
admin.site.register(Student.Student_Details)
admin.site.register(Student.Student_Qualification)