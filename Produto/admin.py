from django.contrib import admin

# Register your models here.
from Produto.models import Produto,Familia

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id','codigo','codigo_Aaxiliar','descricao','familia','unidade','tipo_item','ativo','especificacao',
    'prazo_frete','peso','observacao','comprimento','largura','altura','imagem')



@admin.register(Familia)
class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

# Register your models here.
