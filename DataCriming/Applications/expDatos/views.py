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
        ).values_list('numcarpeta' ,'id_fecha__dia','id_fecha__mes','id_fecha__anio','id_fecha__hora','id_fecha__fecha','id_delito__delito','id_persona__calidadjuridica','id_delito__categoria','id_delito__competencia','id_ubicacion__colonia','id_ubicacion__alcaldia','id_persona__sexo','id_persona__edad','id_persona__tipopersona' )

    df = pd.DataFrame(list(lista), columns=['Numero de carpeta', 'Dia', 'Mes','Año', 'Hora', 'Fecha', 'Delito','Calidad Juridica', 'Categoria', 'Competencia', 'Colonia', 'Alcaldia', 'Sexo', 'Edad', 'Tipo de Persona'])
    #'idCarpeta', 'Dia', 'Mes', 'Año', 'Fecha', 'Hora', 'Delito','calidadjuridica', 'Categoria', 'Competencia', 'Colonia', 'Alcaldia','Sexo', 'Edad', 'TipoPersona', 'longitud', 'latitud'

    print(df.dtypes)
    
    df['Fecha']= pd.to_datetime(df['Fecha'], format="%Y-%m-%d")
    df['Hora']= pd.to_datetime(df['Hora'], format="%H:%M:%S")

    print(df.dtypes)

    profile = ProfileReport(df, title="Analisis EDA", explorative=True)

    profile.to_file("static/AnalisisEDA.html")
    report = profile.to_html()

    context = {'report': report}

    return render(request, 'expDatos/exploratorio.html',context)

    
