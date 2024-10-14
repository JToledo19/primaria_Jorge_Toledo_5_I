from django.db import models

# Create your models here.

class Alumno(models.Model):
    apaterno=models.CharField(max_length=50,verbose_name="Apellido paterno")
    amaterno=models.CharField(max_length=50,verbose_name="Apellido materno")
    nombre=models.CharField(max_length=100,verbose_name="Nombre ()") 
    fecha_nacimiento=models.DateField(verbose_name="Fecha de Nacimiento", null=False,blank=False)
    fecha_ingreso=models.DateField(verbose_name="Fecha de ingreso", null=False,blank=False)