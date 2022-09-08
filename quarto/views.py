from django.shortcuts import render
from quarto.models import Quarto
from django.views.generic import CreateView, UpdateView,ListView, DeleteView,View
from django.urls import reverse_lazy
# Create your views here.

class HomeQuarto(View):
    
    def get(self, request):
        return render(request, 'quarto/home_quarto.html')

class CreateQuarto(CreateView):
    model = Quarto
    template_name = 'create.html'
    fields = ['numero','categoria']
    success_url = reverse_lazy('quartos:home_quarto')

    def form_valid(self, form):
        return super().form_valid(form)

class ListQuarto(ListView):
    template_name: str = 'quarto/list_quartos.html'

    def get_queryset(self):
        queryset = Quarto.objects.all()
        return queryset

class UpdateQuarto(UpdateView):    
    model =Quarto
    template_name = 'create.html'
    fields = ['numero','categoria']
    success_url = reverse_lazy('quartos:home_quarto')

    def form_valid(self, form):
        return super().form_valid(form)

class DeleteQuarto(DeleteView):
    model =Quarto
    template_name = 'quarto/delete_quartos.html'
    success_url = reverse_lazy('quartos:home_quarto')

    def get_success_url(self):
        return reverse_lazy('quartos:home_quarto')
