from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
     path('categorias/',include('categoria.urls',namespace="categorias")),
]
