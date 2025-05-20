from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculo, Mecanico, Trabajo
from .forms import VehiculoForm, MecanicoForm, TrabajoForm

# Create your views here.

# Vehículos

def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'Gestion/listar_vehiculos.html', {'vehiculos': vehiculos})

def crear_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vehiculos')
        
    else: 
        form= VehiculoForm()
        return render (request, 'Gestion/crear_vehiculo.html', {'form': form})
    
    
def editar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    form = VehiculoForm(request.POST or None, instance=vehiculo)
    if form.is_valid():
        form.save()
        return redirect('listar_vehiculos')
    return render(request, 'Gestion/editar_vehiculo.html', {'form': form})

def eliminar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    vehiculo.delete()
    return redirect('listar_vehiculos')

# Mecánicos

def listar_mecanicos(request):
    mecanicos = Mecanico.objects.all()
    return render(request, 'Gestion/listar_mecanicos.html', {'mecanicos': mecanicos})

def crear_mecanico(request):
    if request.method == 'POST':
        form = MecanicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_mecanicos')
    else:
        form = MecanicoForm()
    return render(request, 'Gestion/crear_mecanico.html', {'form': form})

def editar_mecanico(request, id):
    mecanico = get_object_or_404(Mecanico, id=id)
    form = MecanicoForm(request.POST or None, instance=mecanico)
    if form.is_valid():
        form.save()
        return redirect('listar_mecanicos')
    return render(request, 'Gestion/editar_mecanico.html', {'form': form})

def eliminar_mecanico(request, id):
    mecanico = get_object_or_404(Mecanico, id=id)
    mecanico.delete()
    return redirect('listar_mecanicos')

# Trabajos

def listar_trabajos(request):
    trabajos = Trabajo.objects.all()
    return render(request, 'Gestion/listar_trabajos.html', {'trabajos': trabajos})

def crear_trabajo(request):
    if request.method == 'POST':
        form = TrabajoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_trabajos')
    else:
        form = TrabajoForm()
    return render(request, 'Gestion/crear_trabajo.html', {'form': form})

def editar_trabajo(request, id):
    trabajo = get_object_or_404(Trabajo, id=id)
    form = TrabajoForm(request.POST or None, instance=trabajo)
    if form.is_valid():
        form.save()
        return redirect('listar_trabajos')
    return render(request, 'Gestion/editar_trabajo.html', {'form': form})

def eliminar_trabajo(request, id):
    trabajo = get_object_or_404(Trabajo, id=id)
    trabajo.delete()
    return redirect('listar_trabajos')



