from django.db import models
from cliente.models import Cliente
from servicos.models import Servico
from quarto.models import Quarto
# Create your models here.

class DataManager(models.Manager):
    def busca_datas_checkin_checkout(self, _check_in, _check_out):
        self.filter(time__range=(_check_in, _check_out))

class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    status= models.BooleanField(default=False)#Se há uma locação para um determinado quarto e cliente
    quarto = models.ManyToManyField(Quarto)#Só pode fazer reserva se o quarto estiver desocupado
    servicos = models.ManyToManyField(Servico)

    objects = DataManager()

    def __str__(self):
        return str(self.cliente)
    
#Observações: Uma locação só pode ser feita se o quarto estiver livre desde a data de inicio até a data de encerramento
