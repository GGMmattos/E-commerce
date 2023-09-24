from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from . import models


# Create your views here.

class ListaProdutos(ListView): # Listagem dos produtos na home
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'

class DetalheProduto(DetailView):
    model =models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'

class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META['HTTP_REFERER'] # produto será adicionado ao carrinho e irá voltar a paggina anterior.(bate e volta)
        produto_id = self.request.GET.get('id') #Verifica se o produto está cadastrado

        produto = get_list_or_404(models.Produto, id=produto_id)

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = []
            self.request.session.save()
        
        carrinho = self.request.session['carrinho']

        if produto_id in carrinho:
            pass
        else:
            pass

        return  HttpResponse(f' {produto_id}')


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('RemoverDoCarrinho')

class Carrinho(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Carrinho')

class Finalizar(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Finalizar')



