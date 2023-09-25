from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout
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

def Logout(request):
    logout(request)
    return redirect('/')

def Cadastro_perfil (request):
    pass
#     if request.method == 'POST': 
#         form = PerfilForm(request.POST)

#         if form.is_valid(): 
#             form.save()
#             return redirect('/')
#     else:
#         form = PerfilForm() 

#     return render (request, 'perfil/cadastroPerfil.html',{ 
#         'form': form
#     })

# def MeuPerfil(LoginRequiredMixin, View):
#     def get(self, request):
#         user_form = UserUpdateForm(instance=request.user)
#         profile_form = ProfileUpdateForm(instance=request.user.profile)

#         context = {
#             'user_form': user_form,
#             'profile_form': profile_form,
#         }

#         return render(request, 'perfil/meuPerfil.html')
    
#     def post(self, request):
#         user_form = UserUpdateForm(
#             request.POST,
#             instance=request.user
#         )
#         profile_form = ProfileUpdateForm(
#             request.POST,
#             request.FILES,
#             instance=request.user.profile
#         )

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()

#             messages.success(request,'Usuário alterado')

#             return redirect ('/')
#         else:
#             context = {
#                 'user_form' : user_form,
#                 'profile_form' : profile_form
#             }
#             messages.error(request,'Falha ao alterar o usuário')

#             return render(request, 'perfil/meuPerfil.html', context)
    
class Atualizar(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Atualizar')

class Login(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Login')

# class Logout(View):
#     def get(self, *args, **kwargs):
#         return  HttpResponse('Logout')