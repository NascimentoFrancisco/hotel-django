from django.urls import path
from . import views

app_name = "clientes"

urlpatterns = [
    path('',views.HomeCliente.as_view(), name='home_cliente'),
    path('registro/', views.CreateCliente.as_view(), name='create_cliente'),
    path('list/', views.ListCliente.as_view(), name='list_cliente'),
    path('update/<int:pk>/', views.UpdateCliente.as_view(), name='update_cliente'),
    path('delete/<int:pk>/', views.DeleteCliente.as_view(), name='delete_cliente'),            
]