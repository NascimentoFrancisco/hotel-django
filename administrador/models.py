from django.db import models
from django.conf import settings
# Create your models here.

class Administrador(models.Model):
    CARGOS = (
        ('Atendente','Atendente'),
        ('Zelador','Zelador'),
        ('Recepcionista','Recepcionista'),
    )
    name = models.CharField(max_length=253)
    cargo = models.CharField(max_length=253)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuário')