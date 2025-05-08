from django.shortcuts import render # type: ignore
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView  # type: ignore
from .models import Paciente, Doctor, Especialidad, DoctorEspecialidad, Cita
from .serializers import PacienteSerializer, DoctorSerializer, EspecialidadSerializer, DoctorEspecialidadSerializer, CitaSerializer

# Create your views here.


class PacienteListCreateView(ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class PacienteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class DoctorListCreateView(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class EspecialidadListCreateView(ListCreateAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer


class EspecialidadDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer


class DoctorEspecialidadListCreateView(ListCreateAPIView):
    queryset = DoctorEspecialidad.objects.all()
    serializer_class = DoctorEspecialidadSerializer


class DoctorEspecialidadDetailView(RetrieveUpdateDestroyAPIView):
    queryset = DoctorEspecialidad.objects.all()
    serializer_class = DoctorEspecialidadSerializer


class CitaListCreateView(ListCreateAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer


class CitaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
