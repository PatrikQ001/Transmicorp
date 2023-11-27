from django.db import models
from django.core.validators import RegexValidator

ESTADO_UNIDAD = [
    ('Disponible', 'Disponible'),
    ('En Mantenimiento', 'En Mantenimiento'),
    ('En Tránsito', 'En Tránsito')
]

PLACA_REGEX = r'^[A-Za-z0-9]{3}\d{3}$'

class unidades(models.Model):
    Placa_Vehiculo = models.CharField(max_length=100, validators=[RegexValidator(PLACA_REGEX, 'Ingrese una placa válida.')])
    Tipo_de_Vehiculo = models.CharField(max_length=100)
    Capacidad_Carga = models.IntegerField()
    Estado_unidad = models.CharField(max_length=30, choices=ESTADO_UNIDAD)
    Observaciones = models.CharField(max_length=100)

    def __str__(self):
        return f"Unidades {self.id}"
