from django.urls import path
from . import views

app_name = "categorias"

urlpatterns = [
    path('',views.HomeCategoria.as_view(), name='home_curso'),
    path('registro/', views.CreateCategoria.as_view(), name='create_curso'),      
]