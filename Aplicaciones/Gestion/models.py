from django.db import models

class Vehiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    año = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.placa} - {self.marca}"

class Mecanico(models.Model):
    codigo_trabajador = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Trabajo(models.Model):
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"{self.vehiculo.placa} - {self.mecanico.nombre}"
