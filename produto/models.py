from django.db import models
from PIL import Image
import os 
from django.conf import settings
from django.utils.text import slugify


class Produto(models.Model): # criação do modelo - TABELA DO BANCO 
    nome = models.CharField(max_length=255) 
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(
        upload_to='produto_imagem/%Y/&m/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco = models.FloatField()
    estoque = models.PositiveIntegerField(default=1)

    def get_preco_formatado(self):
        return f'R$ {self.preco:.2f}'.replace('.', ',')
    get_preco_formatado.short_description = 'Preço'

    @staticmethod # pala ausência do self
    def relize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size
        
        if original_width <= new_width:
            # print('retornando, largura original maior ou igual que a nova largura')
            img_pil.close()
            return
        
        new_height = round((new_width * original_height)/ original_width) 

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS) # calculo para diminuir a imagem em numero de pixels
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}' #criação do slug - URL do produto
            self.slug = slug
        super().save(*args, **kwargs)

        max_image_size = 800 

        if self.imagem:
            self.relize_image(self.imagem, max_image_size)


    def __str__(self): # So para mostrar os nomes dos produtos :)
        return self.nome


