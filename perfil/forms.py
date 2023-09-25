from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . import models


class SignupForm(UserCreationForm): #Função criada para o cadastro de usuários (usando os campos que ja tem no banco)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    #Daqui pra baixo é estilização do css dos campos que já vem no modelo User
    email = forms.CharField(widget=forms.EmailInput(attrs={ #Estilização do campo email
        'class': 'form-control'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={ #Estilização do campo username
        'class': 'form-control'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={ #Estilização do campo password1
        'class': 'form-control'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={ #Estilização do campo password2
        'class': 'form-control'
    }))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={ #Estilização do campo username
        'class': 'form-control'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={ #Estilização do campo password1
        'class': 'form-control'
    }))

class PerfilForm(UserCreationForm): # Contém dados do perfil do usuário
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ('usuario',)
        


    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data

        