from . import views
from django.urls import path

app_name = "itens"

urlpatterns = [
    path('',views.HomeItens.as_view(), name='home_itens'),
    #Itens do quarto
    path('registro-itens-quarto/', views.CreateItensquarto.as_view(), name='create_itens_quarto'),
    path('list-itens-quarto/', views.ListItensquarto.as_view(), name='list_itens_quarto'),
    path('update-itens-quarto/<int:pk>/', views.UpdateItensquarto.as_view(), name='update-itens-quarto'),
    path('delete-itens-quarto/<int:pk>/', views.DeleteItensquarto.as_view(), name='delete-itens-quarto'),
    #Itens frigobar 
    path('registro-itens-frigobar/', views.CreateItensfrigobar.as_view(), name='create_itens_frigobar'),
    path('list-itens-frigobar/', views.ListItensfrigobar.as_view(), name='list_itens_frigobar'),
    path('update-itens-frigobar/<int:pk>/', views.UpdateItensfrigobar.as_view(), name='update-itens-frigobar'),
    path('delete-itens-frigobar/<int:pk>/', views.DeleteItensfrigobar.as_view(), name='delete-itens-frigobar'),      
]