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
import plotly.express as px
import pandas as pd

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
        """
        mapa = self.request.GET.get('mapa', '')
        categoria = self.request.GET.get('categoria', '')
        alcaldia = self.request.GET.get('alcaldia', '')
        sexo =    self.request.GET.get('sexo', '')
        fecha1 = self.request.GET.get('fInicio', '')
        fecha2 = self.request.GET.get('fFin', '')

        if fecha1 == '': fecha1 = '2000-01-01'
        if fecha2 == '': fecha2 = '2000-01-01'
        
        lista = Hechoscrimen.objects.filter(
            id_delito__categoria__icontains = categoria,
            id_ubicacion__alcaldia__icontains = alcaldia,
            id_persona__sexo__icontains = sexo,
            id_fecha__fecha__range = (fecha1, fecha2)
        )
        return lista
        """
        return []

def chart (request):
        
        grafica = request.GET.get('grafica', '')
        categoria = request.GET.get('categoria', '')
        alcaldia = request.GET.get('alcaldia', '')
        sexo =    request.GET.get('sexo', '')
        fecha1 = request.GET.get('fInicio', '')
        fecha2 = request.GET.get('fFin', '')

        if fecha1 == '': fecha1 = '2021-01-01'
        if fecha2 == '': fecha2 = '2021-01-10'

        if grafica == '1':

            lista = Hechoscrimen.objects.filter(
                id_delito__categoria__icontains = categoria,
                id_ubicacion__alcaldia__icontains = alcaldia,
                id_persona__sexo__icontains = sexo,
                id_fecha__fecha__range = (fecha1, fecha2)
            ).values_list('id_delito__delito', 'id_fecha__fecha')

            df = pd.DataFrame(list(lista), columns=['delito', 'fecha'])

            dfFreq = df.groupby(['delito']).size().to_frame().reset_index()
            dfFreq.columns = ['delito', 'ocurrencia']

            fig = px.pie(dfFreq, values='ocurrencia', names='delito')

        else:
            lista = Hechoscrimen.objects.filter(
                id_delito__categoria__icontains = categoria,
                id_ubicacion__alcaldia__icontains = alcaldia,
                id_persona__sexo__icontains = sexo,
                id_fecha__fecha__range = (fecha1, fecha2)
            ).values_list('id_delito__categoria', 'id_fecha__fecha')

            df = pd.DataFrame(list(lista), columns=['categoria', 'fecha'])

            dfFreq = df.groupby(['fecha']).size().to_frame().reset_index()
            dfFreq.columns = ['fecha', 'ocurrencia']

            if grafica == '0':
                fig = px.line(dfFreq, x='fecha', y='ocurrencia', markers=True)
            
            elif grafica == '2':
                fig = px.bar(dfFreq, x='fecha', y='ocurrencia')

            elif grafica == '3':
                fig = px.histogram(dfFreq, x='fecha', y='ocurrencia')


        fig.update_layout(autosize=True)

        chart = fig.to_html()
        context = {'chart': chart}
        return render(request, 'grafTendencias/tendencias.html', context)
    
        



