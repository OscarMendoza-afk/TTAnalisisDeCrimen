from django.urls import path
from . import views

app_name = "compMapas_app"

#Llamamos a las vistas que se crean localmente en "views"
urlpatterns = [
    path('comparar_mapas/',
    views.CompararMapasTemplateView.as_view(),
    name='compararMapas'),

    path('CompMap',
    views.CompMapa,
    name='CompMapa'),
]
