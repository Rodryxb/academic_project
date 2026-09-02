from rest_framework import viewsets
from .models import Teacher, Course, Student
from .serializers import TeacherSerializer, CourseSerializer, StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher, Course, Student
from .serializers import TeacherSerializer, CourseSerializer, StudentSerializer

# ... (Aquí van tus ViewSets que ya creaste) ...

# --- VISTAS PARA LA INTERFAZ WEB (Solución Error 404) ---
def home_view(request):
    # Esta vista solucionará el error 404 en la ruta "/"
    return render(request, 'academic/home.html')

def courses_view(request):
    return render(request, 'academic/courses.html')

def students_view(request):
    return render(request, 'academic/students.html')