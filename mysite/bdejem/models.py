from django.db import models

# Create your models here.

class Alumnos(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    telf=models.CharField(max_length=9)