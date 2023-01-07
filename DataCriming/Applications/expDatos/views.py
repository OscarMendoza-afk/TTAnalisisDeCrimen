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

def FileExp (request):

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

    #dfE = pd.DataFrame(lista)
    
    #dfE['index'] = dfE.index
    #dfE=dfE.reset_index()
    #dfE=dfE[[0]]
    #dfE=dfE.rename(columns={0 :'Datos'})
    #dfS=dfE.Datos.str.split(pat='_',expand=True)

    #q = lista.values()
    #dfE = pd.DataFrame.from_records(q)

    #dfE = pd.read_csv(r"/home/ozkr/Documentos/alcaldias.csv" ) 

    #print(df.columns)
    #print(df.head)

    profile = ProfileReport(df, title="Analisis EDA", explorative=True)

    report = profile.to_html() 

    context = {'report': report}

    print(report)

    return render(request, 'expDatos/exploratorio.html',context)

