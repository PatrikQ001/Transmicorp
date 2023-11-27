from django.db import models

# Create your models here.
class Proveedor(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=200)
    Correo = models.EmailField()
    Telefono = models.CharField(max_length=9)
    Valoracion = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    TipoProducto = models.CharField(max_length=100)
    DocumentacionLegal = models.FileField(upload_to='documentacion_legal/')  # Cambiado a un campo de texto

    def __str__(self):
        return self.Nombre