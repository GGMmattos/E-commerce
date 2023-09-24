from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from . import models


# Create your views here.
def Cadastro (request):
    return render (request, 'perfil/cadastro.html')

class Criar(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Criar')
    
class Atualizar(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Atualizar')

class Login(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Login')

class Logout(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Logout')