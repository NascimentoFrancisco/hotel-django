import datetime
from django import forms
from locacao.models import Locacao
from quarto.models import Quarto
from datetime import date
from django.shortcuts import get_object_or_404

class LocacaoCreaateForms(forms.ModelForm):
    
    class Meta:
        model = Locacao
        fields = ['cliente','check_in','check_out','quarto','servicos']

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'check_in': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'check_out': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'quarto':forms.SelectMultiple(attrs={'class':'form-control'}),
            'servicos':forms.SelectMultiple(attrs={'class':'form-control'}),
        }
    
    # def clean(self):
    #     super(LocacaoCreaateForms, self).clean()

    #     quarto = self.cleaned_data.get('quarto')
    #     data_hj = date.today()
    #     print(quarto)

    #     _quarto = get_object_or_404(Quarto, numero=quarto.numero)

    #     _quarto.status = True
    #     _quarto.save()
        
    #     return self.changed_data
