from django.db import models

class Produto(models.Model): # criação do modelo - TABELA DO BANCO 
    nome = models.CharField(max_length=255)
    decricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField
    imagem = models.ImageField(
        upload_to='produto_imagem/%Y/&m/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    preco = models.FloatField()