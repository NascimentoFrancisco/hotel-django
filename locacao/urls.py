from django.urls import path
from . import views

app_name = "locacoes"

urlpatterns = [
    path('',views.HomeLcacao.as_view(), name='home_locacao'),
    path('registro/', views.CreateLocacao.as_view(), name='create_locacao'),
    path('list/', views.ListLocacao.as_view(), name='list_locacao'),
    path('update/<int:pk>/', views.UpdateLocacao.as_view(), name='update_locacao'),
    path('delete/<int:pk>/', views.DeleteLocacao.as_view(), name='delete_locacao'),            
]