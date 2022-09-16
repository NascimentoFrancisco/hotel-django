from django.shortcuts import render
from cliente.models import Cliente
from django.views.generic import CreateView, UpdateView,ListView, DeleteView,View
from django.urls import reverse_lazy
# Create your views here.

class HomeCliente(View):
    
    def get(self, request):
        return render(request, 'cliente/home_cliente.html')

class CreateCliente(CreateView):
    model = Cliente
    template_name = 'create.html'
    fields = ['nome','cpf','telefone']
    success_url = reverse_lazy('clientes:list_cliente')

    def form_valid(self, form):
        return super().form_valid(form)

class ListCliente(ListView):
    template_name: str = 'cliente/list_clientes.html'

    def get_queryset(self):
        queryset = Cliente.objects.all()
        return queryset

class UpdateCliente(UpdateView):    
    model =Cliente
    template_name = 'create.html'
    fields = ['nome','cpf','telefone']
    success_url = reverse_lazy('clientes:list_cliente')

    def form_valid(self, form):
        return super().form_valid(form)

class DeleteCliente(DeleteView):
    model =Cliente
    template_name = 'cliente/delete_cliente.html'
    success_url = reverse_lazy('clientes:list_cliente')

    def get_success_url(self):
        return reverse_lazy('clientes:list_cliente')
