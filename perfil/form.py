from django import forms
from django.contrib.auth.models import User
from . import models

class PerfiForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ('usuario',) # exclusão do campo usuários, não estara no cadastro de usuários


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email') # listando campos que iremos utilizar.
    
    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
