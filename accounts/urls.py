from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('create/', views.CrateUser.as_view(), name='create_user'),
    path('login_user/', views.LoginUser.as_view(), name='login_user'),
    path('logout_user/',views.LogoutUser.as_view(),name='logout'),
    #path('',views.HomeCategoria.as_view(), name='home_categoria'),
    #path('registro/', views.CreateCategoria.as_view(), name='create_categoria'),
    #path('list/', views.ListCategoria.as_view(), name='list_categoria'),
    #path('update/<int:pk>/', views.UpdateCategoria.as_view(), name='update_categoria'),
    #path('delete/<int:pk>/', views.DeleteCategoria.as_view(), name='delete_categoria'),            
]