from django.shortcuts import render, redirect, get_list_or_404, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from . import models


# Create your views here.

class ListaProdutos(ListView): # Listagem dos produtos na home
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    

class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'


class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
            )
        produto_id = self.request.GET.get('id')

        if not produto_id:
            messages.error(
                self.request,
                'produto não existe'
            )
            return redirect(http_referer) 

        produto = get_list_or_404(models.Produto, id=produto_id) #TODO: deu ruim por aqui :(
        
        return  redirect(http_referer)





class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('RemoverDoCarrinho')

class Carrinho(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Carrinho')

class Finalizar(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Finalizar')



