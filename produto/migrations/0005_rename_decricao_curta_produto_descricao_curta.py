# Generated by Django 4.2.5 on 2023-09-20 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_produto_estoque'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='decricao_curta',
            new_name='descricao_curta',
        ),
    ]
