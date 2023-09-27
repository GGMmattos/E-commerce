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
from pprint import pprint


# Create your views here.
class ListaProdutos(ListView): # Listagem dos produtos na home
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 12

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
        # if self.request.session.get('carrinho'): // CODIGO PARA APAGAR O CARRINHO
        #     del self.request.session['carrinho']
        #     self.request.session.save()   
    
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista') 
            ) # pega como referencia a tela anterior
        produto_id = self.request.GET.get('id') #verifica o ID da URL

        if not produto_id: # verifica se o produto está cadastrado ou não.
            messages.error(
                self.request,
                'Produto não existe'
            )
            return redirect(http_referer) # Realiza o "bate e volta" ao clicar em adicionar no carrinho
    
        produto = get_object_or_404(models.Produto, id=produto_id) #verifica o id do produto que é desejado adicionar ao carrinho e pega o objeto do mesmo no banco.
        produto_estoque = produto.estoque
        produto_nome = produto.nome
        preco_unitario = produto.preco
        quantidade = 1
        slug = produto.slug
        imagem = produto.imagem

        if produto.estoque < 1: # verifica se há produto no estoque.
            messages.error(
                self.request,
                'Estoque Insuficiente'
            )
            return redirect(http_referer)

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()
        
        carrinho = self.request.session['carrinho']

        if produto_id in carrinho: # se o produto existe no carrinho
            quantidade_carrinho = carrinho[produto_id]['quantidade'] #Adicionando mais um produto no carrinho
            quantidade_carrinho += 1 

            if produto_estoque < quantidade_carrinho:
                messages.warning(
                    self.request,
                    f'Estoque insuficiente para {quantidade_carrinho}x no produto "{produto_nome}". Foi adicionado {produto_estoque}x no seu carrinho.'
                )
                quantidade_carrinho = produto_estoque

            print('QUANTIDADE', quantidade_carrinho)

            carrinho[produto_id]['quantidade'] = quantidade_carrinho
            carrinho[produto_id]['preco_quantitativo'] = preco_unitario * quantidade_carrinho          
        else: # se o produto não existe no carrinho
            carrinho[produto_id] = {
            'produto_id': produto_id,
            'produto_nome': produto_nome,
            'preco_unitario': preco_unitario,
            'preco_quantitativo': preco_unitario,
            'produto_estoque' :produto_estoque,
            'quantidade': 1,
            'slug': slug,
            'imagem': imagem,
            }
        self.request.session.save() # para salvarmos a sessão.

        messages.success( # Mensagem de adicionado com êxito.
            self.request,
            f'Produto {produto_nome} adicionado ao seu carrinho {carrinho[produto_id]["quantidade"]}x'
        )        

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
        contexto = {
            'carrinho': self.request.session.get('carrinho', {})
        }

        return render(self.request, 'produto/carrinho.html', contexto)

class Finalizar(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Finalizar')