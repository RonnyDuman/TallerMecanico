from django.db import models

# Create your models here.
class Vehiculo (models.Model):
    placa=models.CharField(max_length=10, unique= True)
    marca=models.CharField(max_length=50)
    año=models.PositiveIntegerField()

    def _str_(self):
        return f"{self.placa} - {self.marca}"
    
class Mecanico(models.Model):
    codigo_trabajador=models.IntegerField(max_length=10, unique= True)
    nombre = models.CharField(max_length=100)
    especialida=models.CharField(max_length=100)

    def _str_(self):
        return self.nombre

class Trabajo(models.Model):
    mecanico= models.ForeignKey(Mecanico, on_delete=models.CASCADE)
    vehiculo= models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    descripcion=models.TextField()
    fecha=models.DateField()

    def _str_(self):
        return f"{self.vehiculo.placa} - {self.mecanico.nombre}"

