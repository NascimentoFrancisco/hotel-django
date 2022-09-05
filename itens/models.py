from django.db import models

# Create your models here.
class Itens_frigobar(models.Model):
    nome = models.CharField(255)
    preco_item = models.FloatField()

    def __str__(self):
        return self.nome

class Itens_quarto(models.Model):
    nome = models.CharField(255)
    
    def __str__(self):
        return self.nome
