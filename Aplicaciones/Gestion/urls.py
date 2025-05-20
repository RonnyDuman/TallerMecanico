from django.urls import path
from . import views

urlpatterns = [
    # Vehículos
    path('vehiculos/', views.listar_vehiculos, name='listar_vehiculos'),
    path('vehiculos/crear/', views.crear_vehiculo, name='crear_vehiculo'),
    path('vehiculos/editar/<int:id>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('vehiculos/eliminar/<int:id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),

    # Mecánicos
    path('mecanicos/', views.listar_mecanicos, name='listar_mecanicos'),
    path('mecanicos/crear/', views.crear_mecanico, name='crear_mecanico'),
    path('mecanicos/editar/<int:id>/', views.editar_mecanico, name='editar_mecanico'),
    path('mecanicos/eliminar/<int:id>/', views.eliminar_mecanico, name='eliminar_mecanico'),

    # Trabajos
    path('trabajos/', views.listar_trabajos, name='listar_trabajos'),
    path('trabajos/crear/', views.crear_trabajo, name='crear_trabajo'),
    path('trabajos/editar/<int:id>/', views.editar_trabajo, name='editar_trabajo'),
    path('trabajos/eliminar/<int:id>/', views.eliminar_trabajo, name='eliminar_trabajo'),
]
