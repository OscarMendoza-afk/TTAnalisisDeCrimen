from django.contrib import admin

#Importaciones propias
from .models import *

# Register your models here.

admin.site.register(Delito)
admin.site.register(Fecha)
admin.site.register(Persona)
admin.site.register(Ubicacion)
admin.site.register(Hechoscrimen)
