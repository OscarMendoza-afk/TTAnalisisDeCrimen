from django.db import models

# Create your models here.

Sep = '_'

class Delito(models.Model):
    iddelito = models.AutoField(db_column='idDelito', primary_key=True)  # Field name made lowercase.
    delito = models.CharField(db_column='Delito', max_length=300, blank=True, null=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='Categoria', max_length=150, blank=True, null=True)  # Field name made lowercase.
    #competencia = models.CharField(db_column='Competencia', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Delito'

    def __str__(self):
        return self.delito + Sep + self.categoria #+ Sep + self.competencia


class Fecha(models.Model):
    idfecha = models.AutoField(db_column='idFecha', primary_key=True)  # Field name made lowercase.
    #dia = models.IntegerField(db_column='Dia', blank=True, null=True)  # Field name made lowercase.
    #mes = models.CharField(db_column='Mes', max_length=12, blank=True, null=True)  # Field name made lowercase.
    #anio = models.IntegerField(db_column='Anio', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fecha'
    
    def __str__(self):
        return str(self.fecha) + Sep + str(self.hora) #+ Sep + str(self.dia) + Sep + self.mes + Sep + str(self.anio)


class Geopoint(models.Model):
    idgeopoint = models.AutoField(db_column='idGeoPoint', primary_key=True)  # Field name made lowercase.
    longitud = models.FloatField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GeoPoint'

    def __str__(self):
        return str(self.longitud) + Sep + str(self.latitud)



class Persona(models.Model):
    idpersona = models.AutoField(db_column='idPersona', primary_key=True)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.
    #tipopersona = models.CharField(db_column='TipoPersona', max_length=15, blank=True, null=True)  # Field name made lowercase.
    #calidadjuridica = models.CharField(db_column='CalidadJuridica', max_length=35, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Persona'
    
    def __str__(self):
        return self.sexo + Sep + str(self.edad)# + Sep + self.tipopersona + Sep + self.calidadjuridica


class Ubicacion(models.Model):
    idubicacion = models.AutoField(db_column='idUbicacion', primary_key=True)  # Field name made lowercase.
    alcaldia = models.CharField(db_column='Alcaldia', max_length=35, blank=True, null=True)  # Field name made lowercase.
    colonia = models.CharField(db_column='Colonia', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ubicacion'
    
    def __str__(self):
        return self.alcaldia + Sep + self.colonia


class Hechoscrimen(models.Model):
    idhechoscrimen = models.AutoField(db_column='idHechosCrimen', primary_key=True)  # Field name made lowercase.
    #numcarpeta = models.IntegerField(db_column='NumCarpeta')  # Field name made lowercase.
    id_delito = models.ForeignKey(Delito, models.DO_NOTHING, db_column='id_Delito')  # Field name made lowercase.
    id_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='id_Persona')  # Field name made lowercase.
    id_fecha = models.ForeignKey(Fecha, models.DO_NOTHING, db_column='id_Fecha')  # Field name made lowercase.
    id_ubicacion = models.ForeignKey(Ubicacion, models.DO_NOTHING, db_column='id_Ubicacion')  # Field name made lowercase.
    id_geopoint = models.ForeignKey(Geopoint, models.DO_NOTHING, db_column='id_GeoPoint')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HechosCrimen'
    
    def __str__(self):
        return str(self.id_delito) + Sep + str(self.id_persona) + Sep + str(self.id_fecha) + Sep + str(self.id_ubicacion) + Sep + str(self.id_geopoint)# + Sep + str(self.numcarpeta)
