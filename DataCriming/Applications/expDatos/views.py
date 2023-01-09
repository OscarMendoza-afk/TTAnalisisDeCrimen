#Importaciones django
from django.shortcuts import render

#Importaciones propias
from django.views.generic import (
    ListView,
    TemplateView
    )
from .models import *

from django.urls import reverse_lazy


#importar pandas

import pandas as pd

from pandas_profiling import ProfileReport

class ExploratorioTemplateView(ListView):
    template_name = "expDatos/exploratorio.html"

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

def report (request):

    categoria = request.GET.get('categoria', '')
    alcaldia = request.GET.get('alcaldia', '')
    sexo =    request.GET.get('sexo', '')
    fecha1 = request.GET.get('fInicio', '')
    fecha2 = request.GET.get('fFin', '')

    if fecha1 == '': fecha1 = '2000-01-01'
    if fecha2 == '': fecha2 = '2000-01-01'
    
    lista = Hechoscrimen.objects.filter(
            id_delito__categoria__icontains = categoria,
            id_ubicacion__alcaldia__icontains = alcaldia,
            id_persona__sexo__icontains = sexo,
            id_fecha__fecha__range = (fecha1, fecha2)
        ).values_list('id_fecha__dia','id_fecha__mes','id_fecha__anio','id_fecha__hora','id_fecha__fecha','id_delito__delito','id_persona__calidadjuridica','id_delito__categoria','id_delito__competencia','id_ubicacion__colonia','id_ubicacion__alcaldia','id_persona__sexo','id_persona__edad','id_persona__tipopersona' )

    df = pd.DataFrame(list(lista), columns=['dia', 'mes','anio', 'fecha', 'hora', 'delito','calidadjuridica', 'categoria', 'competencia', 'colonia', 'alcaldia','sexo', 'edad', 'tipopersona'])
    #'idCarpeta', 'Dia', 'Mes', 'Año', 'Fecha', 'Hora', 'Delito','calidadjuridica', 'Categoria', 'Competencia', 'Colonia', 'Alcaldia','Sexo', 'Edad', 'TipoPersona', 'longitud', 'latitud'
    df.drop_duplicates(inplace=True)

    profile = ProfileReport(df, title="Analisis EDA", explorative=True)
    
    nav = '<nav class="navbar navbar-default navbar-fixed-top"><div class=container-fluid><div class=navbar-header><button type=button class="navbar-toggle collapsed" data-toggle=collapse data-target=#navbar aria-expanded=false aria-controls=navbar><span class=sr-only>Toggle navigation</span><span class=icon-bar></span><span class=icon-bar></span><span class=icon-bar></span></button><a class="navbar-brand anchor" href=#top>Analisis EDA</a></div><div id=navbar class="navbar-collapse collapse"><ul class="nav navbar-nav navbar-right"><li><a href=#overview>Overview</a></li><li><a href=#variables-dropdown>Variables</a></li><li><a href=#interactions>Interactions</a></li><li><a href=#correlations_tab>Correlations</a></li><li><a href=#missing>Missing values</a></li><li><a href=#sample>Sample</a></li></ul></div></div></nav>'


    #profile.to_file("AnalisisEDA.html")
    report = profile.to_html()

    #LeftstrReport = str(report).rstrip('<nav class="navbar navbar-default navbar-fixed-top">')

    #RightstrReport = str(report).lstrip('</nav>')

    #report = LeftstrReport + RightstrReport
    
    #report = str(report).replace(nav , " ")
    #report = str(report).replace("navbar navbar-default", " text ")

    

    context = {'report': report}

    return render(request, 'expDatos/exploratorio.html',context)

