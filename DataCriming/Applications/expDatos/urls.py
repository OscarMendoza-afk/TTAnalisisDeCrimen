from django.urls import path
from . import views

app_name = "expDatos_app"

#Llamamos a las vistas que se crean localmente en "views"
urlpatterns = [
    path('analisis_exploratorio/',
    views.ExploratorioTemplateView.as_view(),
    name='exploratorio'),

]
