from django.urls import path
from . import views

app_name = "quartos"

urlpatterns = [
     path('',views.HomeQuarto.as_view(), name='home_quarto'),
     path('registro/', views.CreateQuarto.as_view(), name='create_quarto'),
     path('list/', views.ListQuarto.as_view(), name='list_quarto'),
     path('list-quartos-livres/',views.ListQuartoLivres.as_view(),name='list_quartos_livres'),
     path('update/<int:pk>/', views.UpdateQuarto.as_view(), name='update_quarto'),
     path('delete/<int:pk>/', views.DeleteQuarto.as_view(), name='delete_quarto'),            
]