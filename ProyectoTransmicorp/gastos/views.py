from django.shortcuts import render, redirect, get_object_or_404
from .models import gastos
from .forms import GastosForm

def crear_gasto(request):
    if request.method == 'POST':
        form = GastosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_gasto')
    else:
        form = GastosForm()
    return render(request, 'crear_gasto.html', {'form': form})

def ver_gasto(request, pk):
    gasto = get_object_or_404(gastos, pk=pk)
    return render(request, 'ver_gasto.html', {'gasto': gasto})

def editar_gasto(request, pk):
    gasto = get_object_or_404(gastos, pk=pk)
    if request.method == 'POST':
        form = GastosForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            return redirect('ver_gasto', pk=pk)
    else:
        form = GastosForm(instance=gasto)
    return render(request, 'editar_gasto.html', {'form': form, 'gasto': gasto})

def eliminar_gasto(request, pk):
    gasto = get_object_or_404(gastos, pk=pk)
    if request.method == 'POST':
        gasto.delete()
        return redirect('lista_gasto')
    return render(request, 'eliminar_gasto.html', {'gasto': gasto})

def lista_gasto(request):
    gasto = gastos.objects.all()
    return render(request, 'lista_gasto.html', {'gasto': gasto})