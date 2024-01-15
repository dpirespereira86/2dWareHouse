# Generated by Django 5.0.1 on 2024-01-14 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produto', '0003_alter_produto_especificacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='codigo_Aaxiliar',
        ),
        migrations.AddField(
            model_name='produto',
            name='auto_solicitacao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='produto',
            name='codigo_Auxiliar',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='codigo',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='produto',
            name='especificacao',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='fornecedor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='observacao',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='tipo_item',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='produto',
            name='unidade',
            field=models.CharField(choices=[('Cj', 'Conjunto'), ('Cx', 'Caixa'), ('Dz', 'Dúzia'), ('Fd', 'Fardo'), ('Fl', 'Folha'), ('Gl', 'Galão'), ('Lt', 'Lote'), ('Jg', 'Jogo'), ('Kg', 'Kilograma'), ('L', 'Litro'), ('Lta', 'Lata'), ('M', 'Metro'), ('Mil', 'Milheiro'), ('Par', 'Par'), ('Pct', 'Pacote'), ('Pç', 'Peça'), ('Res', 'Resma'), ('Rl', 'Rolo'), ('Ton', 'Tonelada'), ('Und', 'Unidade'), ('Vd', 'Vidro'), ('M³', 'Metro_cubico'), ('M²', 'Metro_quadrado')], max_length=30),
        ),
    ]