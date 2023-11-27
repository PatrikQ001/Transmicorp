
from django import forms
from .models import factura

class FacturaForm(forms.ModelForm):
    class Meta:
        model = factura
        fields = ['Orden_de_trabajo', 'Fecha_Emision', 'Id_cliente', 'Importe', 'Pago_de_detraccion', 'Documento_factura']
        widgets = {
            'IGV': None,
            'Detraccion': None,
        }