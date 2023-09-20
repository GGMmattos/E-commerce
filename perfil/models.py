from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

import re #expressão regulares
from utils.validacpf import valida_cpf # importando função para validade o CPF

# Create your models here.
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name = 'Usuário')
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, verbose_name = 'CPF') # apenas números
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=8, verbose_name = 'CEP') #apenas números
    cidade = models.CharField(max_length=30)
    estado = models.CharField(
        max_length=2,
        default='PR',
        choices= (
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),    
        )
    )

    def __str__(self):
        return f'{self.usuario}'
    

    def clean(self):
        error_messages = {}

        if not valida_cpf(self.cpf):
            error_messages['cpf'] = 'Digite um CPF válido'
        
        if re.search(r'[^0-9]', self.cep) or len(self.cep) < 8: # se CEP n contém somente números e o len < 8
            error_messages['cep'] = 'CEP inválido, digite os 8 dígitos do CEP.'
        
        if error_messages:
            raise ValidationError(error_messages)


    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'