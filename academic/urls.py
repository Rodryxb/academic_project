from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView, LogoutView  # <-- Importamos las vistas de Auth
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, CourseViewSet, StudentViewSet, home_view, courses_view, students_view

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    # Endpoints de la API
    path('api/', include(router.urls)),
    
    # Sistema de Autenticación (Login / Logout)
    path('login/', LoginView.as_view(template_name='academic/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Rutas de la Interfaz Web
    path('', home_view, name='home'),
    path('cursos/', courses_view, name='courses'),
    path('estudiantes/', students_view, name='students'),
    
    # Ruta Comodín (Siempre al final)
    re_path(r'^.*$', home_view),
]