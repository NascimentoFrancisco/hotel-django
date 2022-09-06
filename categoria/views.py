from django.shortcuts import render
from categoria.models import Categoria
from django.views.generic import CreateView, UpdateView,ListView, DeleteView,View
from django.urls import reverse_lazy
# Create your views here.

class HomeCategoria(View):
    
    def get(self, request):
        return render(request, 'categoria/home_categoria.html')

class CreateCategoria(CreateView):
    model = Categoria
    template_name = 'create.html'
    fields = ['nome','preco','frigobar','itens_quarto']
    success_url = reverse_lazy('home.html')

    def form_valid(self, form):
        return super().form_valid(form)
