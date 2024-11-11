from django.contrib import admin

# Register your models here.
from .models import Categoria, Producto, Cliente, Orden

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Orden)
