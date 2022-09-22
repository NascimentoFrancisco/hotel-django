from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import HomeView, erro_view_404,erro_view_403, erro_view_500

from django.urls import re_path as url
from django.conf import settings
from django.views.static import serve

handler404 = erro_view_404
handler403 = erro_view_403
handler500 = erro_view_500

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
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
