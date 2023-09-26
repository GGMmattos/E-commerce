from django import forms
from .models import Produto

class NovoProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'descricao_curta', 'descricao_longa', 'imagem', 'preco', 'estoque', 'slug')

    nome = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    descricao_curta = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    descricao_longa = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))

    preco = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

    slug = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    estoque = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))