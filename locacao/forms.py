import datetime
from django import forms
from locacao.models import Locacao

class LocacaoCreaateForms(forms.ModelForm):
    
    class Meta:
        model = Locacao
        fields = ['cliente','check_in','check_out','status','quarto','servicos']

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'check_in': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'check_out': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'status': forms.CheckboxInput(),
            'quarto':forms.SelectMultiple(attrs={'class':'form-control'}),
            'servicos':forms.SelectMultiple(attrs={'class':'form-control'}),
        }