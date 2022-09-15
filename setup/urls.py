from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('categorias/',include('categoria.urls',namespace="categorias")),
    path('itens/',include('itens.urls',namespace='itens')),
    path('clientes/',include('cliente.urls',namespace='clientes')),
    path('quartos/',include('quarto.urls',namespace='quartos')),
    path('servicos/',include('servicos.urls',namespace='servicos')),
    path('locacoes/',include('locacao.urls',namespace='locacoes')),
]
