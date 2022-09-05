from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)#Será posto um validador de cpf nesse campo
    telefone = models.CharField(max_length=16)
    
    def __str__(self):
        return self.nome
