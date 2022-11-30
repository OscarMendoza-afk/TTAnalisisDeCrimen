#Importaciones django
from django.shortcuts import render

#Importaciones propias
from django.views.generic import (
    ListView,
    TemplateView
    )

from django.urls import reverse_lazy

class ExploratorioTemplateView(TemplateView):
    template_name = "expDatos/exploratorio.html"

