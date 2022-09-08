from django.shortcuts import render
from itens.models import Itens_quarto,Itens_frigobar
from django.views.generic import CreateView, UpdateView,ListView, DeleteView,View
from django.urls import reverse_lazy
# Create your views here.

class HomeItens(View):
    
    def get(self, request):
        return render(request, 'itens/home_itens.html')

class CreateItensfrigobar(CreateView):
    model = Itens_frigobar
    template_name = 'create.html'
    fields = ['nome','preco_item']
    success_url = reverse_lazy('itens:home_itens')

    def form_valid(self, form):
        return super().form_valid(form)

class ListItensfrigobar(ListView):
    template_name: str = 'itens/list_itensfrigobar.html'

    def get_queryset(self):
        queryset = Itens_frigobar.objects.all()
        return queryset

class UpdateItensfrigobar(UpdateView):    
    model =Itens_frigobar
    template_name = 'create.html'
    fields = ['nome','preco_item']
    success_url = reverse_lazy('itens:home_itens')

    def form_valid(self, form):
        return super().form_valid(form)

class DeleteItensfrigobar(DeleteView):
    model =Itens_frigobar
    template_name = 'itens/delete_item_frigobar.html'
    success_url = reverse_lazy('itens:home_itens')

    def get_success_url(self):
        return reverse_lazy('itens:home_itens')

#Itens do quarto
class CreateItensquarto(CreateView):
    model = Itens_quarto
    template_name = 'create.html'
    fields = ['nome',]
    success_url = reverse_lazy('itens:home_itens')

    def form_valid(self, form):
        return super().form_valid(form)

class ListItensquarto(ListView):
    template_name: str = 'itens/list_itensquarto.html'

    def get_queryset(self):
        queryset = Itens_quarto.objects.all()
        return queryset

class UpdateItensquarto(UpdateView):    
    model =Itens_quarto
    template_name = 'create.html'
    fields = ['nome',]
    success_url = reverse_lazy('itens:home_itens')

    def form_valid(self, form):
        return super().form_valid(form)

class DeleteItensquarto(DeleteView):
    model =Itens_quarto
    template_name = 'itens/delete_item_quarto.html'
    success_url = reverse_lazy('itens:home_itens')

    def get_success_url(self):
        return reverse_lazy('itens:home_itens')
