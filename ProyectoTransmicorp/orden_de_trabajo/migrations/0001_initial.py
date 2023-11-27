# Generated by Django 4.2 on 2023-09-10 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden_trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RUC_cliente', models.CharField(max_length=11)),
                ('Id_Conductor', models.CharField(max_length=12)),
                ('Id_Vehiculo', models.CharField(max_length=8)),
                ('Origen', models.CharField(max_length=20)),
                ('Destino', models.CharField(max_length=20)),
                ('Detalles', models.CharField(max_length=20)),
                ('Peso', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Tipo', models.CharField(max_length=20)),
                ('Fecha_Emision', models.DateField()),
                ('Descripcion', models.CharField(max_length=300)),
                ('Monto_Cotizacion', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Estado', models.BooleanField()),
                ('Tipo_orden_de_trabajo', models.CharField(choices=[('1', 'No tercerizada'), ('2', 'Tercerizada')], max_length=20)),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.clientes')),
            ],
        ),
    ]
