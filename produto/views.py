from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from . import models
from .forms import NovoProdutoForms
from produto.models import Produto


# Create your views here.
class ListaProdutos(ListView): # Listagem dos produtos na home
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 6

class Busca(ListaProdutos):
    def get_queryset(self, *args, **kwargs):
        termo = self.request.GET.get('termo')
        qs = super().get_queryset(*args, **kwargs)

        if not termo:
            return qs
        
        qs = qs.filter( Q(nome__icontains=termo) | Q(descricao_curta__icontains=termo) | Q(descricao_longa__icontains=termo))
        return qs
        
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

@login_required
def new(request):
    if request.method == 'POST':
        form = NovoProdutoForms(data=request.POST, files=request.FILES)

        if form.is_valid():
            item = form.save(commit=False) #Cria o item sem o created_by
            item.created_by = request.user #Coloca o created_by como o usuário logado
            item.save() #Salva no banco

            return redirect('produto:detalhe', item.slug)
    else:
        form = NovoProdutoForms()

    return render(request, 'produto/novoProduto.html', {
        'form': form,
        'title': 'Novo Produto',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Produto, pk=pk)
    item.delete()
    
    return redirect ('produto:lista')

class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('RemoverDoCarrinho')

class Carrinho(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Carrinho')

class Finalizar(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Finalizar')