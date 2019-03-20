from django.db import models


class Persona(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=80)
    telefono = models.CharField(max_length=12)
    edad = models.IntegerField()
    email = models.EmailField()
    domicilio = models.TextField()
