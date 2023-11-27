from django.db import models

# Create your models here.

OPCIONES_ESTADO_LICENCIA =[
    ('1','Vigente'),
    ('2','Suspendida'),
    ('3','Vencida'),
    ('4','Invalida')
]

TIPO_LICENCIA =[
        ('1','A-I'),
        ('2','A-IIa'),
        ('3','A-IIb'),
        ('4','A-IIIa'),
        ('5','A-IIIb'),
        ('6','A-IIIc'),
        ('7','B-I'),
        ('8','B-IIa'),
        ('9','B-IIb'),
        ('10','B-IIc')
]

OPCIONES_RENDIMIENTO = [
    ('1', 'Excelente'),
    ('2', 'Bueno'),
    ('3', 'Regular'),
    ('4', 'Necesita Mejorar'),
    ('5', 'Deficiente.'),
]


class Empleados(models.Model):
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    DNI = models.IntegerField()
    Telefono = models.IntegerField()
    Correo = models.CharField(max_length=40)
    Estado_Licencia = models.CharField(max_length=20, default='Valor Predeterminado', choices=OPCIONES_ESTADO_LICENCIA)
    Observaciones =  models.CharField(max_length=100)
    Rendimiento =  models.CharField(max_length=50, default='Valor Predeterminado', choices=OPCIONES_RENDIMIENTO)
    Licencia = models.CharField(max_length=50, default='Valor Predeterminado', choices=TIPO_LICENCIA)
    

    def __str__(self):
        return f"Empleados {self.id}"
    
