from django.db import models
from django.conf import settings

class Bike(models.Model):
    nome = models.CharField(primary_key=True, max_length=20, default='')
    modelo = models.CharField(max_length=20, default='')
    quantidade = models.IntegerField(default=0)
    color = models.CharField(max_length=10, choices=settings.COLOR)
    def __unicode__(self):
        return self.nome
