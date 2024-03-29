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
import geopandas as gpd
import plotly.express as px
import json
from sklearn.cluster import DBSCAN, MeanShift
from django_plotly_dash import DjangoDash

class CrearMapasTemplateView(ListView):
    template_name = "crearMapas/crearMapas.html"
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

def mapaC (request):

    mapa= request.GET.get('mapa', '')
    categoria = request.GET.get('categoria', '')
    alcaldia = request.GET.get('alcaldia', '')
    sexo =    request.GET.get('sexo', '')
    fecha1 = request.GET.get('fInicio', '')
    fecha2 = request.GET.get('fFin', '')

    if fecha1 == '': fecha1 = '2021-01-01'
    if fecha2 == '': fecha2 = '2021-01-10'
    
    lista = Hechoscrimen.objects.filter(
        id_delito__categoria__icontains = categoria,
        id_ubicacion__alcaldia__icontains = alcaldia,
        id_persona__sexo__icontains = sexo,
        id_fecha__fecha__range = (fecha1, fecha2)
    ).values_list('id_delito__delito','id_fecha__fecha','id_fecha__hora','id_delito__categoria','id_ubicacion__colonia','id_ubicacion__alcaldia','id_geopoint__longitud','id_geopoint__latitud')
    

    df = pd.DataFrame(list(lista), columns=['delito','fecha', 'hora','categoria', 'colonia', 'alcaldia','longitud','latitud'])


    #print(poligonos)

    if mapa == '0': #Grfica de Coropletas

        if alcaldia == '':
            
            with open('AlcaldiasshapeCDMX.json') as data_file:    poligonos= json.load(data_file) 
            dfA=df["alcaldia"].value_counts()
            dfA=dfA.to_frame()

            dfA['index'] = dfA.index
            dfA=dfA.reset_index()
            dfA=dfA[['index','alcaldia']]

            dfA=dfA.rename(columns={'index' :'alcaldia', 'alcaldia' :'NumDelitos'})
            #dfF=pd.merge(dfA, gdf, on='Alcaldia')
            fig = px.choropleth(data_frame=dfA, 
                            geojson=poligonos, 
                            locations='alcaldia', # nombre de la columna del Dataframe
                            featureidkey='properties.nomgeo',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                            color='NumDelitos', #El color depende de las cantidades
                            color_continuous_scale="blues",
                            width=1000, 
                            height=600
                        )
            fig.update_geos(showcountries=True, showcoastlines=True, showland=True, fitbounds="locations")

            fig.update_layout(
                title_text = 'Mapa de Coropletas del Crimen en la CDMX',
                font=dict(
                    #family="Courier New, monospace",
                    family="Ubuntu",
                    size=18,
                    color="#7f7f7f"
                )
            )
        
        if alcaldia != '':
            with open('coloniasCDMX.json') as data_file:    poligonos= json.load(data_file) 

            dfA=df["colonia"].value_counts()
            dfA=dfA.to_frame()

            dfA['index'] = dfA.index
            dfA=dfA.reset_index()
            dfA=dfA[['index','colonia']]

            dfA=dfA.rename(columns={'index' :'colonia', 'colonia' :'NumDelitos'})
            #dfF=pd.merge(dfA, gdf, on='Alcaldia')
            fig = px.choropleth(data_frame=dfA, 
                            geojson=poligonos, 
                            locations='colonia', # nombre de la columna del Dataframe
                            featureidkey='properties.nombre',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                            color='NumDelitos', #El color depende de las cantidades
                            color_continuous_scale="blues",
                            width=1000, 
                            height=600
                        )
            fig.update_geos(showcountries=True, showcoastlines=True, showland=True, fitbounds="locations")

            fig.update_layout(
                mapbox_style="open-street-map",
                title_text = 'Mapa de Coropletas del Crimen en la CDMX',
                font=dict(
                    #family="Courier New, monospace",
                    family="Ubuntu",
                    size=18,
                    color="#7f7f7f"
                )
            )

    elif mapa == '1': #Mapa de calor

        df['Info'] = '<br>Delito:' + df['delito'].astype(str) + '<br>Fecha:' + df['fecha'].astype(str)

        fig = px.density_mapbox(df, lon='longitud', lat='latitud',  radius=5,
                        title="Mapa de calor de",
                        color_continuous_scale="inferno",
                        center=dict(lon=-99.1374477062327, lat=19.402765630374645), zoom=9,                        
                        hover_name="alcaldia",
                        hover_data=["Info"],
                        mapbox_style="carto-positron",
                        height=600)
                        
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    elif mapa == '2': #puntos

        df['Info'] = '<br>Delito:' + df['delito'].astype(str) + '<br>Fecha:' + df['fecha'].astype(str)
        fig = px.scatter_mapbox(df, lon='longitud', lat='latitud', hover_name="alcaldia", hover_data=["Info"],center=dict(lon=-99.1374477062327, lat=19.402765630374645), zoom=10,
                        color_discrete_sequence=["blue"], height=600)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    elif mapa == '3':

        df['Info'] = '<br>Delito:' + df['delito'].astype(str) + '<br>Fecha:' + df['fecha'].astype(str)

        df['lon'] = df['longitud']*1000
        df['lat'] = df['latitud']*1000

        df['DBSCAN'] = DBSCAN(eps=8, min_samples=8).fit_predict(df[['lon', 'lat']])

        print(df)

        fig = px.scatter_mapbox(df, lon='longitud', lat='latitud', color='DBSCAN', hover_name="alcaldia", hover_data=["Info"],center=dict(lon=-99.1374477062327, lat=19.402765630374645), zoom=10,
                        color_discrete_sequence=["blue"], height=600)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        

    elif mapa == '4':

        df['Info'] = '<br>Delito:' + df['delito'].astype(str) + '<br>Fecha:' + df['fecha'].astype(str)

        df['lon'] = df['longitud']*100
        df['lat'] = df['latitud']*100

        df['MS'] = MeanShift().fit_predict(df[['lon', 'lat']])

        print(df)

        fig = px.scatter_mapbox(df, lon='longitud', lat='latitud', color='MS', hover_name="alcaldia", hover_data=["Info"],center=dict(lon=-99.1374477062327, lat=19.402765630374645), zoom=10,
                        color_discrete_sequence=["blue"], height=600)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


    mapaC = fig.to_html()

    context = {'mapaC': mapaC}
    return render(request, 'crearMapas/crearMapas.html', context)

    
