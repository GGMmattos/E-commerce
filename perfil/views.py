from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from . import models
from . import forms
from .forms import SignupForm
from .forms import PerfilForm



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

def Cadastro_perfil (request): #TODO CRIADO PARA TEST RS
    if request.method == 'POST': 
        form = PerfilForm(request.POST)

        if form.is_valid(): 
            form.save()
            return redirect('/')
    else:
        form = PerfilForm() 

    return render (request, 'perfil/cadastro.html',{ 
        'form': form
    })


    
class Atualizar(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Atualizar')

class Login(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Login')

class Logout(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Logout')