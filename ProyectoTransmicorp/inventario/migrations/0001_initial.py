# Generated by Django 4.2 on 2023-09-10 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_Inventario', models.CharField(max_length=12)),
                ('Nombre', models.CharField(max_length=100)),
                ('FechaIngreso', models.DateField()),
                ('Cantidad', models.IntegerField()),
                ('NumeroRegistro', models.IntegerField()),
                ('Descripcion', models.CharField(max_length=100)),
                ('TiempoVida', models.IntegerField()),
                ('Ambiente', models.FileField(upload_to='archivos/')),
                ('Estado', models.BooleanField()),
            ],
        ),
    ]
