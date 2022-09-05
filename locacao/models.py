from django.db import models
from cliente.models import Cliente
from servicos.models import Servico
from quarto.models import Quarto
# Create your models here.

class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente)
    check_in = models.DateField()
    check_out = models.DateField()
    quarto = models.ManyToManyField(Quarto)
    servicos = models.ManyToManyField(Servico)

    def __str__(self):
        return self.id