from django.contrib import admin
from .models import Pedido, ItemPedido


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInline
    ]

#Ao visualizar um pedido verifica todos os itens deste pedido

# Register your models here.
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido)
