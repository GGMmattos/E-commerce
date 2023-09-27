from django.template import Library

register = Library()


@register.filter
def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.', ',') #utilizado para realizar a formatação dos preços dos produtos

@register.filter
def card_total_qtd(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])


@register.filter
def card_total(carrinho):
    return sum(
        item.get('preco_quantitativo')
        for item in carrinho.values()
    )