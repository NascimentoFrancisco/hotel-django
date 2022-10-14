from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def valida_tamanho_cpf(value):
    if len(value) < 11:
        raise ValidationError(f'CPF inválido, contém apenas {len(value)} dígitos.')

def valida_tamanho_telefone(value):
    if len(value) < 11:
        raise ValidationError(f'Telefone inválido, contém apenas {len(value)} dígitos.')

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11,validators = [valida_tamanho_cpf])#Será posto um validador de cpf nesse campo
    telefone = models.CharField(max_length=16,validators = [valida_tamanho_telefone])
    
    def __str__(self):
        return self.nome
