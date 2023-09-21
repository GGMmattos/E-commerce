from django.contrib import admin
from .models import Produto
# Register your models here.


class ProdutoAdmin (admin.ModelAdmin):
    list_display  = [
        'nome', 'descricao_curta', 'get_preco_formatado',
    ]
    
admin.site.register(Produto, ProdutoAdmin)
