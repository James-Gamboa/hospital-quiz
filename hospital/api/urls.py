from django.urls import path  # type: ignore
from .views import (
    PacienteListCreateView, PacienteDetailView,
    DoctorListCreateView, DoctorDetailView,
    EspecialidadListCreateView, EspecialidadDetailView,
    DoctorEspecialidadListCreateView, DoctorEspecialidadDetailView,
    CitaListCreateView, CitaDetailView,
    UserRegistrationView
)

urlpatterns = [
    path('pacientes/', PacienteListCreateView.as_view(),
         name='paciente-list-create'),
    path('pacientes/<int:pk>/', PacienteDetailView.as_view(), name='paciente-detail'),

    path('doctores/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctores/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),

    path('especialidades/', EspecialidadListCreateView.as_view(),
         name='especialidad-list-create'),
    path('especialidades/<int:pk>/', EspecialidadDetailView.as_view(),
         name='especialidad-detail'),

    path('doctores-especialidades/', DoctorEspecialidadListCreateView.as_view(),
         name='doctor-especialidad-list-create'),
    path('doctores-especialidades/<int:pk>/',
         DoctorEspecialidadDetailView.as_view(), name='doctor-especialidad-detail'),

    path('citas/', CitaListCreateView.as_view(), name='cita-list-create'),
    path('citas/<int:pk>/', CitaDetailView.as_view(), name='cita-detail'),

    path('register/', UserRegistrationView.as_view(), name='user_registration'),
]
