from django.db import models
from categoria.models import Categoria
# Create your models here.

class Quarto(models.Model):
    numero = models.IntegerField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self):
        return self.numero