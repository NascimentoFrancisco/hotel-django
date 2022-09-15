import datetime
from django import forms
from locacao.models import Locacao

class LocacaoCreaateForms(forms.ModelForm):
    
    class Meta:
        model = Locacao
        fields = ['cliente','check_in','check_out','status','quarto','servicos']

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'check_in': forms.DateInput(format='%d/%m/%Y'),#Error
            'check_out': forms.DateInput(format='%d/%m/%Y'),#Error
            'status': forms.BooleanField(required=False),
            'quarto':forms.Select(attrs={'class':'form-control'}),
            'servicos':forms.SelectMultiple(attrs={'class':'form-control'}),
        }