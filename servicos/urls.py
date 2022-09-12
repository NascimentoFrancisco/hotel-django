from django.urls import path
from . import views

app_name = "servicos"

urlpatterns = [
    path('',views.HomeServico.as_view(), name='home_servico'),
    path('registro/', views.CreateServico.as_view(), name='create_servico'),
    path('list/', views.ListServico.as_view(), name='list_servico'),
    path('update/<int:pk>/', views.UpdateServico.as_view(), name='update_servico'),
    path('delete/<int:pk>/', views.DeleteServico.as_view(), name='delete_servico'),            
]