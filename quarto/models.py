from django.db import models
from categoria.models import Categoria
# Create your models here.

class Quarto(models.Model):
    numero = models.IntegerField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    status= models.BooleanField(default=False)#Se há um quarto disponível em periodo de tempo

    def filtra_status(self, status:bool) -> str:
        if self.status:
            return "Ocupado"
        return "Livre"

    def __str__(self):
        return "Nº "+str(self.numero)+", Categoria: "+str(self.categoria)+", Valor: "+str(self.categoria.preco)+", Status: "+self.filtra_status(self.status)