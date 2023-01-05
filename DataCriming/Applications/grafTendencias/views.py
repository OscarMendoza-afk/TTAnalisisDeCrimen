#Importaciones django
from django.shortcuts import render

#Importaciones propias
from django.views.generic import (
    ListView,
    TemplateView
    )

#Importacion de tablas
from .models import *

from django.urls import reverse_lazy


class InicioTemplateView(TemplateView):
    template_name = "inicio.html"

class MotivacionTemplateView(TemplateView):
    template_name = "motivacion.html"

class AyudaTemplateView(TemplateView):
    template_name = "ayuda.html"

class TendenciasTemplateView(ListView):
    template_name = "grafTendencias/tendencias.html"

    queryset = Hechoscrimen.objects.filter(
        id_delito__categoria = 'HOMICIDIO DOLOSO',
        id_ubicacion__alcaldia = 'TLALPAN',
        id_persona__sexo = 'Masculino',
        id_fecha__fecha__range = ('2020-01-01', '2020-03-01')
    )



