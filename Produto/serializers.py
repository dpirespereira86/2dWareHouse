from rest_framework import serializers
from .models import Produto,Familia
from Armazem.serializers import EstoqueProdutoSerializers



class ProdutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields=('id','codigo','codigo_Aaxiliar','descricao','familia','unidade','tipo_item','ativo','especificacao',
    'prazo_frete','peso','observacao','comprimento','largura','altura','imagem')

class ProdutoEstoqueSerializers(serializers.ModelSerializer):
    estoques= EstoqueProdutoSerializers
    class Meta:
        model = Produto
        fields=('id','codigo','estoques')

class FamiliaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Familia
        fields = ('nome',)