#Importaciones django
from django.shortcuts import render

#Importaciones propias
from django.views.generic import (
    ListView,
    TemplateView
    )

from django.urls import reverse_lazy


class InicioTemplateView(TemplateView):
    template_name = "inicio.html"

class MotivacionTemplateView(TemplateView):
    template_name = "motivacion.html"

class AyudaTemplateView(TemplateView):
    template_name = "ayuda.html"

class TendenciasTemplateView(TemplateView):
    template_name = "grafTendencias/tendencias.html"

