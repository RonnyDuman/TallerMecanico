from django.contrib import admin
from .models import Vehiculo, Mecanico, Trabajo

# Register your models here.
admin.site.register(Vehiculo)
admin.site.register(Mecanico)
admin.site.register(Trabajo)