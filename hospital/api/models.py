from django.db import models # type: ignore

# Create your models here.


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    anios_experiencia = models.IntegerField()
    especialidades = models.ManyToManyField(
        Especialidad, through='DoctorEspecialidad')

    def __str__(self):
        return self.nombre


class DoctorEspecialidad(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.doctor.nombre} - {self.especialidad.nombre}"


class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()

    def __str__(self):
        return f"Cita de {self.paciente.nombre} con {self.doctor.nombre} el {self.fecha} a las {self.hora}"
