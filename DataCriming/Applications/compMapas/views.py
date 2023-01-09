#Importaciones django
from django.shortcuts import render

#Importaciones propias
from django.views.generic import (
    ListView,
    TemplateView
    )
from .models import *
from django.urls import reverse_lazy

#importar librerias necesarias
from dash import Dash, dcc, html, Input, Output
import geopandas as gpd
import pandas as pd
import plotly.express as px
import json
from sklearn.cluster import DBSCAN, MeanShift
from django_plotly_dash import DjangoDash
import plotly.graph_objects as go

class CompararMapasTemplateView(ListView):
    template_name = "compMapas/compMapas.html"
    context_object_name = "valores"

    def get_queryset(self):
        
        return []


def CompMapa (request):

    mapa= request.GET.get('mapa', '')

    categoria1 = request.GET.get('categoria1', '')
    alcaldia1 = request.GET.get('alcaldia1', '')
    sexo1 =    request.GET.get('sexo1', '')
    fechaI1 = request.GET.get('fInicio1', '')
    fechaF1 = request.GET.get('fFin1', '')

    if fechaI1 == '': fechaI1 = '2021-01-01'
    if fechaF1 == '': fechaF1 = '2021-01-10'

    categoria2 = request.GET.get('categoria2', '')
    alcaldia2 = request.GET.get('alcaldia2', '')
    sexo2 =    request.GET.get('sexo2', '')
    fechaI2 = request.GET.get('fInicio2', '')
    fechaF2 = request.GET.get('fFin2', '')

    if fechaI2 == '': fechaI2 = '2021-01-01'
    if fechaF2 == '': fechaF2 = '2021-01-10'
    
    lista1 = Hechoscrimen.objects.filter(
        id_delito__categoria__icontains = categoria1,
        id_ubicacion__alcaldia__icontains = alcaldia1,
        id_persona__sexo__icontains = sexo1,
        id_fecha__fecha__range = (fechaI1, fechaF1)
    ).values_list('id_delito__delito','id_fecha__fecha','id_fecha__hora','id_delito__categoria','id_ubicacion__colonia','id_ubicacion__alcaldia','id_geopoint__longitud','id_geopoint__latitud')
    
    lista2 = Hechoscrimen.objects.filter(
        id_delito__categoria__icontains = categoria2,
        id_ubicacion__alcaldia__icontains = alcaldia2,
        id_persona__sexo__icontains = sexo2,
        id_fecha__fecha__range = (fechaI2, fechaF2)
    ).values_list('id_delito__delito','id_fecha__fecha','id_fecha__hora','id_delito__categoria','id_ubicacion__colonia','id_ubicacion__alcaldia','id_geopoint__longitud','id_geopoint__latitud')
    
    df = pd.DataFrame(list(lista1), columns=['delito','fecha', 'hora','categoria', 'colonia', 'alcaldia','longitud','latitud'])
    dfm1 = pd.DataFrame(list(lista1), columns=['delito','fecha', 'hora','categoria', 'colonia', 'alcaldia','longitud','latitud'])
    dfm2 = pd.DataFrame(list(lista2), columns=['delito','fecha', 'hora','categoria', 'colonia', 'alcaldia','longitud','latitud'])

    
    with open('AlcaldiasshapeCDMX.json') as data_file:    poligonos= json.load(data_file) 

    locs=df['alcaldia']
    #print(poligonos)

    if mapa == '1': #Mapa de puntos

        dfm1['Info'] = '<br>Delito:' + dfm1['delito'].astype(str) + '<br>Fecha:' + dfm1['fecha'].astype(str)
        dfm1['TP'] = 1
        
        dfm2['Info'] = '<br>Delito:' + dfm2['delito'].astype(str) + '<br>Fecha:' + dfm2['fecha'].astype(str)
        dfm2['TP'] = 2

        df = pd.concat([dfm1, dfm2], axis=0)
    
        print(df)

        fig = px.scatter_mapbox(df, lon='longitud', lat='latitud', color='TP', hover_name="alcaldia", hover_data=["Info"],center=dict(lon=-99.1374477062327, lat=19.402765630374645), zoom=10,
                        color_discrete_sequence=["blue"], height=600)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


    elif mapa == '2': #Mapa HS1
        
        dfm1['Info'] = '<br>Delito:' + dfm1['delito'].astype(str) + '<br>Fecha:' + dfm1['fecha'].astype(str)
        dfm1['lon'] = dfm1['longitud']*1000
        dfm1['lat'] = dfm1['latitud']*1000
        dfm1['DBSCAN'] = DBSCAN(eps=8, min_samples=8).fit_predict(dfm1[['lon', 'lat']])

        dfm1.loc[dfm1.DBSCAN >= 0, 'DBSCAN'] = 1
        
        dfm2['Info'] = '<br>Delito:' + dfm2['delito'].astype(str) + '<br>Fecha:' + dfm2['fecha'].astype(str)
        dfm2['lon'] = dfm2['longitud']*1000
        dfm2['lat'] = dfm2['latitud']*1000
        dfm2['DBSCAN'] = DBSCAN(eps=8, min_samples=8).fit_predict(dfm2[['lon', 'lat']])

        dfm2.loc[dfm2.DBSCAN >= 0, 'DBSCAN'] = 2

        df = pd.concat([dfm1, dfm2], axis=0)
    
        print(df)

        fig = px.scatter_mapbox(df, lon='longitud', lat='latitud', color='DBSCAN', hover_name="alcaldia", hover_data=["Info"],center=dict(lon=-99.1374477062327, lat=19.402765630374645), zoom=10,
                        color_discrete_sequence=["blue"], height=600)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            

    elif mapa == '3': #puntos

        dfm1['Info'] = '<br>Delito:' + dfm1['delito'].astype(str) + '<br>Fecha:' + dfm1['fecha'].astype(str)
        dfm1['lon'] = dfm1['longitud']*1000
        dfm1['lat'] = dfm1['latitud']*1000
        dfm1['MS'] = MeanShift().fit_predict(dfm1[['lon', 'lat']])

        dfm1.loc[dfm1.MS >= 0, 'MS'] = 1
        
        dfm2['Info'] = '<br>Delito:' + dfm2['delito'].astype(str) + '<br>Fecha:' + dfm2['fecha'].astype(str)
        dfm2['lon'] = dfm2['longitud']*1000
        dfm2['lat'] = dfm2['latitud']*1000
        dfm2['MS'] = MeanShift().fit_predict(dfm2[['lon', 'lat']])

        dfm2.loc[dfm2.MS >= 0, 'MS'] = 2

        df = pd.concat([dfm1, dfm2], axis=0)

        fig = px.scatter_mapbox(df, lon='longitud', lat='latitud', color='MS', hover_name="alcaldia", hover_data=["Info"],center=dict(lon=-99.1374477062327, lat=19.402765630374645), zoom=10,
                        color_discrete_sequence=["blue"], height=600)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


    mapaC = fig.to_html()

    context = {'mapaC': mapaC}
    
    return render(request, 'compMapas/compMapas.html', context,)
 

    

