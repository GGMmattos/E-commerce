# Generated by Django 4.2.5 on 2023-09-25 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0008_alter_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produto_imagem/%Y/&m/'),
        ),
    ]