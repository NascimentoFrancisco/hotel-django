from django.shortcuts import render
from accounts.models import User
from accounts.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, FormView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.


class CrateUser(CreateView):

    model = User
    template_name = 'accounts/create_user.html'
    form_class = UserCreationForm #UserAdminCreationForm
    success_url = reverse_lazy('accounts:login_user')
    
    def form_valid(self, form):
        messages.info(
            self.request, "Cadastro realizado com sucesso! Faça seu login."
        )
        return super().form_valid(form)

class LoginUser(LoginView):

    model = User
    template_name = 'accounts/login.html'


class LogoutUser(LogoutView):

    template_name = 'accounts/logout_user.html'

