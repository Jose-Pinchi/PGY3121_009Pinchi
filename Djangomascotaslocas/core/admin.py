from django.contrib import admin
from .models import Genero, Cliente, Tamanio, Producto

# Register your models here.

admin.site.register(Genero)
admin.site.register(Cliente)
admin.site.register(Tamanio)
admin.site.register(Producto)