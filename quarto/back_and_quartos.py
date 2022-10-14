from datetime import date
from quarto.models import Quarto
from locacao.models import Locacao
from datetime import date
from django.utils import timezone

def filtra_livres(request, quartos):

    data_hj = timezone.now()
    
    for quarto in quartos:
        
        if quarto.status:
            print("Ocupado")
        else:
            print("Livre")
            