from django.db import models
from itens.models import Itens_frigobar,Itens_quarto
# Create your models here.
    
class Categoria(models.Model):
    nome= models.CharField(max_length=200)
    preco = models.FloatField()
    frigobar = models.ManyToManyField(Itens_frigobar)
    itens_quarto = models.ManyToManyField(Itens_quarto)

    def __str__(self):
        return self.nome