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
from django_plotly_dash import DjangoDash
import plotly.graph_objects as go

class CompararMapasTemplateView(ListView):
    template_name = "compMapas/compMapas.html"
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

    
    with open('/home/ozkr/Documentos/AlcaldiasshapeCDMX.json') as data_file:    poligonos= json.load(data_file) 

    locs=df['alcaldia']
    #print(poligonos)

    if mapa == '1': #Mapa calor

        dfm1['Info'] = '<br>Delito:' + dfm1['delito'].astype(str) + '<br>Fecha:' + dfm1['fecha'].astype(str)

        # Generamos la figura del mapa
        fig = go.Figure()
        # Recorremos los datos del archivo csv y extraemos sus coordenadas,
        # etiquetas a mostrar y especificamos características del marcador
        for i in dfm1:
            fig.add_trace(go.Scattergeo(
            lon = dfm1['longitud'],
            lat = dfm1['latitud'],
            text = dfm1['categoria'],
            marker = dict(
            color = 'Blue',
            line_color='black',
            line_width=0.3,
            sizemode = 'area'
        )))

        for i in dfm2:
            fig.add_trace(go.Scattergeo(
            lon = dfm2['longitud'],
            lat = dfm2['latitud'],
            text = dfm2['categoria'],
            marker = dict(
            color = 'Red',
            line_color='black',
            line_width=0.3,
            sizemode = 'area'
        )))

        fig.update_layout(

            title_text = 'Población en las ciudades del mundo, año 2025',
            mapbox_style="carto-positron",
            showlegend = False,
            autosize=True,
            height=700,
            geo=dict(
            center=dict(
            lon=-99.1374477062327,
            lat=19.402765630374645),
            projection_scale=300,
            showsubunits = True,
            showland = True,
            showcountries = True
            ))


    elif mapa == '2': #Mapa puntos

            dfFreq = df.groupby(['delito']).size().to_frame().reset_index()
            dfFreq.columns = ['delito', 'ocurrencia']

            locs=df['alcaldia']

            fig=go.Figure()


            fig.add_trace(go.Choroplethmapbox(
                                geojson=poligonos, 
                                locations=locs, # nombre de la columna del Dataframe
                                featureidkey='properties.nomgeo',
                                z=dfFreq['ocurrencia'],
                                colorscale='blues'))

            for i in dfm1:
                fig.add_trace(go.Scattergeo(
                lon = dfm1['longitud'],
                lat = dfm1['latitud'],
                text = dfm1['categoria'],
                marker = dict(
                color = 'Blue',
                line_color='black',
                line_width=0.3,
                sizemode = 'area'
                )))

            for i in dfm2:
                fig.add_trace(go.Scattergeo(
                lon = dfm2['longitud'],
                lat = dfm2['latitud'],
                text = dfm2['categoria'],
                marker = dict(
                color = 'Red',
                line_color='black',
                line_width=0.3,
                sizemode = 'area'
                )))

            """
            fig.update_layout(

            title_text = 'Población en las ciudades del mundo, año 2025',
            mapbox_style="carto-positron",
            showlegend = False,
            autosize=True,
            height=700,
            geo=dict(
            center=dict(
            lon=-99.1374477062327,
            lat=19.402765630374645),
            projection_scale=300,
            showsubunits = True,
            showland = True,
            showcountries = True
            ))
            """

            
            fig.update_layout(mapbox_style="carto-positron",
                                    mapbox_zoom=3.4,
                                    mapbox_center = {"lat": 19.402765630374645, "lon": -99.1374477062327})
            

    elif mapa == '3': #puntos

        print("DBscan")

    elif mapa == '4': 

        app = DjangoDash('hotspotuno')


        layout= app.layout = html.Div([
            html.H4("Interactive color mode option with Dash"),
            html.P("Color mode:"),
            dcc.RadioItems(
                id='discrete-color-x-color-mode', 
                value='capa', 
                options=['discrete', 'continuous'],
            ),
            dcc.Graph(id="discrete-color-x-graph"),
        ])


        @app.callback(
            Output("discrete-color-x-graph", "figure"), 
            Input("discrete-color-x-color-mode", "value"))


        def generate_chart(mode):
            if mode == 'discrete':
                x=[1, 2, 3, 4] 
                y=[1, 4, 9, 16]
            else:
                x=[1, 2, 5, 4] 
                y=[1, 6, 10, 16]

            fig = px.line(x, y, title=r'$\alpha_{1c} = 352 \pm 11 \text{ km s}^{-1}$')
            
            return {'data': [fig], 'layout': layout}

        

        print("HotSpot1")


    mapaC = fig.to_html()

    context = {'mapaC': mapaC}
    
    return render(request, 'compMapas/compMapas.html', context,)
 

    

