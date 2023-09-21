from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Criar.as_View(), name='criar'),
    path('atualizar/', views.Atualizar.as_View(), name='atualizar'),
    path('login/', views.Login.as_View(), name='login'),
    path('logout/', views.Logout.as_View(), name='logout'),
    
]