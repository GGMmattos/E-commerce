from django.db import models
from django.contrib.auth.models  import User

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # Caso o usuário venha a sem excluido seus pedidos tbm serão.
    total = models.FloatField()
    status = models.CharField(
        default="C",
        max_length=1, 
        choices=(
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
        )
    )

    def __str__(self):
        return f'Pedido N. {self.pk}'
    

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE) #  Caso o Pedido venha a sem excluido seus itens tbm serão.
    nome_produto = models.CharField(max_length=255)
    id_produto = models.PositiveBigIntegerField()
    preco = models.FloatField() 
    imagem = models.CharField(max_length=2000) # Campo adicionado para que produtos que ja foram comprados e teve sua imagem atualizada não atualizem o produto nos itens dos clientes

    def __str__(self):
        return f'Item do {self.pedido}'

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'


