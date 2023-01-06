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
    context_object_name = "valores"

    def get_queryset(self):

        grafica = self.request.GET.get('grafica', '')
        categoria = self.request.GET.get('categoria', '')
        alcaldia = self.request.GET.get('alcaldia', '')
        sexo =    self.request.GET.get('sexo', '')
        fecha1 = self.request.GET.get('fInicio', '')
        fecha2 = self.request.GET.get('fFin', '')

        if fecha1 == '': fecha1 = '2000-01-01'
        if fecha2 == '': fecha2 = '2000-01-01'
        
        lista = Hechoscrimen.objects.filter(
            id_delito__categoria = categoria,
            id_ubicacion__alcaldia = alcaldia,
            id_persona__sexo = sexo,
            id_fecha__fecha__range = (fecha1, fecha2)
        )
        return lista
        
    
        



