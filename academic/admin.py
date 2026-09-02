from django.contrib import admin
from .models import Teacher, Student, Course, StudentCourse

# Registramos los modelos para que aparezcan en el panel
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(StudentCourse)