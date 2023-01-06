from django.urls import path
from . import views

app_name = "grafTendencias_app"

#Llamamos a las vistas que se crean localmente en "views"
urlpatterns = [
    path('',
    views.InicioTemplateView.as_view(),
    name='inicio'),

    path('motivacion/',
    views.MotivacionTemplateView.as_view(),
    name='motivacion'),

    path('ayuda/',
    views.AyudaTemplateView.as_view(),
    name='ayuda'),

    path('graficador_tendencias/',
    views.TendenciasTemplateView.as_view(),
    name='tendencias'),

    path('grafica',
    views.chart ,
    name='chart'),

]
