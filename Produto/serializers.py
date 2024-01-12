from rest_framework import serializers
from .models import Produto,Familia



class ProdutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields=('id','codigo','codigo_Aaxiliar','descricao','familia','unidade','tipo_item','ativo','especificacao',
    'prazo_frete','peso','observacao','comprimento','largura','altura','imagem')


class FamiliaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Familia
        fields = ('nome',)