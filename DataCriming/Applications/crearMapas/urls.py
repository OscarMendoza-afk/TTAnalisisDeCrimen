from django.urls import path
from . import views

app_name = "crearMapas_app"

#Llamamos a las vistas que se crean localmente en "views"
urlpatterns = [
    path('creador_mapas/',
    views.CrearMapasTemplateView.as_view(),
    name='crearMapas'),

    path('mapa',
    views.mapaC ,
    name='mapaC'),

]

