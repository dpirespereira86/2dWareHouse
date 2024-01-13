from rest_framework import serializers
from .models import Unidade,MOVIMENTACAO,Estoque,Item,Posicao

class UnidadeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields=('nome',)


class EstoqueProdutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields=( 'posicao','quantidade',)


class EstoqueSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields=( 'posicao','produto','quantidade',)

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields=( 'id','codigo','codigo_interno','descricao','quantidade','movimentacao',)

class PosicaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Posicao
        fields=('id','unidade','nome','rua','predio','nivel','sequencia')

class MovimentacaoSerializers(serializers.ModelSerializer):
    itens = ItemSerializers(many=True)
    class Meta:
        model = MOVIMENTACAO
        fields=('id','tipo','date','operador','posicao','itens')