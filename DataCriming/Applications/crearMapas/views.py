#Importaciones django
from django.shortcuts import render

#Importaciones propias
from django.views.generic import (
    ListView,
    TemplateView
    )
from .models import *

from django.urls import reverse_lazy

class CrearMapasTemplateView(ListView):
    template_name = "crearMapas/crearMapas.html"

    def get_queryset(self):
        lista = Hechoscrimen.objects.filter(
            id_delito__categoria = 'HOMICIDIO DOLOSO',
            id_ubicacion__alcaldia = 'TLALPAN',
            id_persona__sexo = 'Masculino',
            id_fecha__fecha__range = ('2020-01-01', '2020-03-01')
        )
        return lista
