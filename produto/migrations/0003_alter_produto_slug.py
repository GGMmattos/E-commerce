# Generated by Django 4.2.5 on 2023-09-20 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_produto_descricao_longa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
