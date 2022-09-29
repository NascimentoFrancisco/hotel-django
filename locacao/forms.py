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
            'cliente': forms.Select(attrs={'class':'form-control'}),
            'check_in': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'check_out': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'quarto':forms.SelectMultiple(attrs={'class':'form-control'}),
            'servicos':forms.SelectMultiple(attrs={'class':'form-control'}),
        }
    
    '''def clean(self):
        super(LocacaoCreaateForms, self).clean()

        quartos = self.cleaned_data.get('quarto')
        check_in = self.cleaned_data.get('check_in')
        check_out = self.cleaned_data.get('check_out')
        
        
        for quarto in quartos:
            if not quarto.status:
                print(f'Quarto {quarto.numero} livre')
                #_quarto = get_object_or_404(Quarto, pk=quarto.id)
                #_quarto.status = True
                #_quarto.save()
            else:
                self.errors['quarto'] = self.error_class([f'Quarto {quarto.numero} ocupado!'])
        
        return self.changed_data'''
