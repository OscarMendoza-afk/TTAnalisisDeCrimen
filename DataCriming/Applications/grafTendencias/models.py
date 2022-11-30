from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Prueba (models.Model):
    titulo = models.CharField(max_length = 50)
    subtitulo = models.CharField(max_length = 50)