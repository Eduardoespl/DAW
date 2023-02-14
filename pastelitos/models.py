from django.db import models

# Create your models here.
class pastel(models.Model):
    cubierta=models.CharField(max_length=20, blank=False, default=None)
    precio=models.FloatField(blank=False, default=None)
    sabor=models.CharField(max_length=40, blank=False, default=None)
    peso=models.FloatField(blank=False, default=None)
    pisos=models.IntegerField(null=False, blank=False)
    tipo=models.CharField(max_length=40, blank=False, default=None)