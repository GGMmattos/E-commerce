from django.urls import path, include
from . import views

app_name = 'perfil'

urlpatterns = [
    path('cadastro/', views.Cadastro, name='criar'),
    path('atualizar/', views.Atualizar.as_view(), name='atualizar'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    
]