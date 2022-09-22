from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
    
    def get(self, request):
        return render(request, 'home.html')

def erro_view_404(request, *args, **kwargs):
    return render(request,'pages_erros/erro_404.html')

def erro_view_403(request, *args, **kwargs):
    return render(request,'pages_erros/erro_403.html')

def erro_view_500(request, *args, **kwargs):
    return render(request,'pages_erros/erro_500.html')