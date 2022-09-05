from django.contrib import admin
from categoria.models import Categoria, Itens_frigobar, Itens_quarto
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Itens_frigobar)
admin.site.register(Itens_quarto)
