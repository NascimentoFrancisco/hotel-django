from datetime import date
from quarto.models import Quarto
from locacao.models import Locacao

def filtra_livres(quartos):
    for quarto in quartos:
        if quarto.status:
            print("Ocupado")
        else:
            print("Livre")
            