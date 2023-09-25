from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .forms import LoginForm

app_name = 'perfil'

urlpatterns = [
    path('cadastro/', views.Cadastro, name='criar'),
    path('cadastro-perfil/', views.Cadastro_perfil, name='criarPerfil'),
    path('atualizar/', views.Atualizar.as_view(), name='atualizar'),
    path('login/',auth_views.LoginView.as_view(template_name='perfil/entrar.html' ,authentication_form=LoginForm), name='login'),
    path('logout/', views.Logout, name='logout'),
]