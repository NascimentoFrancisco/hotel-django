from django.db import models

# Create your models here.

class Servico(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.FloatField()
    
    def __str__(self):
        return self.nome
