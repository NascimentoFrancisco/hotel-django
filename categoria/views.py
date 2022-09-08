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
    success_url = reverse_lazy('categorias:home_categoria')

    def form_valid(self, form):
        return super().form_valid(form)

class ListCategoria(ListView):
    template_name: str = 'categoria/list_categoria.html'

    def get_queryset(self):
        queryset = Categoria.objects.all()
        return queryset

class UpdateCategoria(UpdateView):    
    model =Categoria
    template_name = 'create.html'
    fields = ['nome','preco','frigobar','itens_quarto']
    success_url = reverse_lazy('categorias:home_categoria')

    def form_valid(self, form):
        return super().form_valid(form)

class DeleteCategoria(DeleteView):
    model =Categoria
    template_name = 'categoria/delete_categoria.html'
    success_url = reverse_lazy('categorias:home_categoria')

    def get_success_url(self):
        return reverse_lazy('categorias:home_categoria')
