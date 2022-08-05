from django.db import models

# Create your models here.

class RedesSocialesCatalogo(models.Model):
    descripcion = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'redessocialescatalogo'

class Encuesta(models.Model):
    correo = models.CharField(max_length=100, null=True)
    edad = models.IntegerField( null=True)
    sexo = models.CharField(max_length=100)
    fecha = models.DateField(null=True,blank=True)

    class Meta:
        db_table = 'encuesta'

class Pregunta(models.Model):
    encuesta = models.ForeignKey(Encuesta, on_delete=models.PROTECT, null=True)
    redSocial = models.ForeignKey(RedesSocialesCatalogo, on_delete=models.PROTECT, null=True)
    isFavorita = models.BooleanField(default = 0)
    tiempo = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'pregunta'