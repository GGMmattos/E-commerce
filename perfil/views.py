from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from . import models
from . import forms
from .forms import SignupForm


# Create your views here.
def Cadastro (request):
    if request.method == 'POST': #Checa se o botão "enviar" do forms foi clicado.
        form = SignupForm(request.POST)

        if form.is_valid(): #Salva os dados se eles forem válidos
            form.save()
            return redirect('/')
    else:
        form = SignupForm() 

    return render (request, 'perfil/cadastro.html',{ #Renderiza a página cadastro.html
        'form': form
    })

class BasePerfil(View):
    template_name = 'perfil/criar.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.contexto = {
            'userform': forms.UserForm(
                data= self.request.POST or None
            ), 
            'perfilform': forms.PerfiForm(
                data= self.request.POST or None
            )
        }

        self.renderizar = render(self.request, self.template_name, self.contexto)
    
    def get(self, *args, **kwargs):
        return self.renderizar


class Criar(BasePerfil):
    pass
    
class Atualizar(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Atualizar')

class Login(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Login')

class Logout(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Logout')