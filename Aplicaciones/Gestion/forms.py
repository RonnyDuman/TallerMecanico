from django import forms
from .models import Vehiculo, Mecanico, Trabajo

class VehiculoForm(forms.ModelForm):
     class Meta:
        model = Vehiculo
        fields = ['placa', 'marca', 'año']
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class MecanicoForm(forms.ModelForm):
     class Meta:
         model = Mecanico
         fields = ['codigo_trabajador', 'nombre', 'especialidad']
         widgets = {
            'codigo_trabajador': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
        }
         
class TrabajoForm(forms.ModelForm):
     class Meta:
          model = Trabajo
          fields = ['mecanico', 'vehiculo', 'descripcion', 'fecha']
          widgets = {
            'mecanico': forms.Select(attrs={'class': 'form-control'}),
            'vehiculo': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }