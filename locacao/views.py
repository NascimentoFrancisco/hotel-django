from django.shortcuts import render
from locacao.models import Locacao
from django.views.generic import CreateView, UpdateView,ListView, DeleteView,View
from django.urls import reverse_lazy
from locacao.forms import LocacaoCreaateForms
# Create your views here.

class HomeLcacao(View):
    
    def get(self, request):
        return render(request, 'locacao/home_locacao.html')

class CreateLocacao(CreateView):#Falta por uma vefificação para validar se o quarto escolido pode ou não ser inserido na locação
    model = Locacao
    template_name = 'locacao/create_locacao.html'
    form_class = LocacaoCreaateForms
    #fields = ['cliente','check_in','check_out','status','quarto','servicos']
    success_url = reverse_lazy('locacoes:list_locacao')

    def form_valid(self, form):
        return super().form_valid(form)

class ListLocacao(ListView):
    template_name: str = 'locacao/list_locacoes.html'

    def get_queryset(self):
        queryset = Locacao.objects.all()
        return queryset

class UpdateLocacao(UpdateView):    
    model = Locacao
    template_name = 'create.html'
    form_class = LocacaoCreaateForms
    success_url = reverse_lazy('locacoes:list_locacao')

    def form_valid(self, form):
        return super().form_valid(form)

class DeleteLocacao(DeleteView):#falta uma validação para verificar se o quarto pode ser deletado...Pagamento
    model = Locacao
    template_name = 'locacao/delete_locacao.html'
    success_url = reverse_lazy('locacoes:list_locacao')

    def get_success_url(self):
        return reverse_lazy('locacoes:list_locacao')
