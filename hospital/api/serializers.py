from .models import Paciente, Doctor, Especialidad, DoctorEspecialidad, Cita
from rest_framework import serializers  # type: ignore
from datetime import date


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

    def validate_edad(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "La edad debe ser un número positivo.")
        return value


class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'


class DoctorEspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorEspecialidad
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    especialidades = EspecialidadSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = '__all__'

    def validate_anios_experiencia(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Los años de experiencia no pueden ser negativos.")
        return value


class CitaSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = Cita
        fields = '__all__'

    def validate(self, data):
        # {
        #     "paciente": 1,
        #     "doctor": 2,
        #     "fecha": "2025-05-07",
        #     "motivo": ""
        # }

        # {
        #     "paciente": 1,
        #     "doctor": 2,
        #     "fecha": null,  # Falta la fecha
        #     "hora": null,  # Falta la hora
        #     "motivo": "Consulta general"
        # }
        if data['fecha'] is None or data['hora'] is None:
            raise serializers.ValidationError(
                "La fecha y la hora son obligatorias para una cita.")

        # {
        #     "paciente": 1,
        #     "doctor": 2,
        #     "fecha": "2025-05-07",
        #     "hora": "10:00:00",
        #     "motivo": "Consulta general"
        # }
        if data['fecha'] < date.today():
            raise serializers.ValidationError(
                "La fecha de la cita no puede ser en el pasado.")

        # {
        #     "paciente": 1,
        #     "doctor": 2,
        #     "fecha": "2025-05-10",
        #     "hora": "10:00:00",
        #     "motivo": ""
        # }
        if not data['motivo'].strip():
            raise serializers.ValidationError(
                "El motivo de la cita no puede estar vacío.")

        # {
        #     "paciente": -1,
        #     "doctor": 2,
        #     "fecha": "2025-05-10",
        #     "hora": "10:00:00",
        #     "motivo": "Consulta general"
        # }
        if data['paciente'].id <= 0:
            raise serializers.ValidationError(
                "El ID del paciente debe ser un número positivo.")

        # {
        #     "paciente": 1,
        #     "doctor": -2,
        #     "fecha": "2025-05-10",
        #     "hora": "10:00:00",
        #     "motivo": "Consulta general"
        # }
        if data['doctor'].id <= 0:
            raise serializers.ValidationError(
                "El ID del doctor debe ser un número positivo.")

        return data
