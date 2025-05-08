from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Paciente, Doctor, Especialidad, DoctorEspecialidad, Cita

admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Especialidad)
admin.site.register(DoctorEspecialidad)
admin.site.register(Cita)

def create_default_roles():
    roles = ['admin', 'empleado', 'cliente']
    for role in roles:
        Group.objects.get_or_create(name=role)

create_default_roles()
