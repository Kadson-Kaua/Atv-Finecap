from django.forms import ModelForm
from django import forms
from .models import Reserva

class ReservaForm(ModelForm):
    quitado = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Reserva
        exclude = ['user']
        fields = '__all__'
        widgets = {
            'cnpj' : forms.TextInput(attrs={'class': 'form-control' }),
            'nome_empresa' : forms.TextInput(attrs={'class': 'form-control' }),
            'categoria_empresa' : forms.TextInput(attrs={'class': 'form-control' }),
            'stand': forms.Select(attrs={'class': 'form-control' }),
        }
