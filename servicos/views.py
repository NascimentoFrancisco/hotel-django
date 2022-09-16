from django.shortcuts import render
from servicos.models import Servico
from django.views.generic import CreateView, UpdateView,ListView, DeleteView,View
from django.urls import reverse_lazy
# Create your views here.

class HomeServico(View):
    
    def get(self, request):
        return render(request, 'servico/home_servico.html')

class CreateServico(CreateView):
    model = Servico
    template_name = 'create.html'
    fields = ['nome','valor']
    success_url = reverse_lazy('servicos:list_servico')

    def form_valid(self, form):
        return super().form_valid(form)

class ListServico(ListView):
    template_name: str = 'servico/list_servicos.html'

    def get_queryset(self):
        queryset = Servico.objects.all()
        return queryset

class UpdateServico(UpdateView):    
    model =Servico
    template_name = 'create.html'
    fields = ['nome','valor']
    success_url = reverse_lazy('servicos:list_servico')

    def form_valid(self, form):
        return super().form_valid(form)

class DeleteServico(DeleteView):
    model =Servico
    template_name = 'servico/delete_servico.html'
    success_url = reverse_lazy('servicos:list_servico')

    def get_success_url(self):
        return reverse_lazy('servicos:list_servico')
