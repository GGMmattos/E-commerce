# Generated by Django 4.2.5 on 2023-09-20 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_alter_produto_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='estoque',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]