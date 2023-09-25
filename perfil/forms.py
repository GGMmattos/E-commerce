from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

#Comentei essas duas classes porque acho que não vai precisa delas.

# class PerfiForm(forms.ModelForm):
#     class Meta:
#         model = models.Perfil
#         fields = '__all__'
#         exclude = ('usuario',) # exclusão do campo usuários, não estara no cadastro de usuários


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username', 'password', 'email') # listando campos que iremos utilizar.
    
#     def clean(self, *args, **kwargs):
#         data = self.data
#         cleaned = self.cleaned_data

class SignupForm(UserCreationForm): #Função criada para o cadastro de usuários (usando os campos que ja tem no banco)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))