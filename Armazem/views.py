from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Unidade,Posicao,MOVIMENTACAO,Item,Estoque
from .serializers import UnidadeSerializers,PosicaoSerializers,MovimentacaoSerializers,ItemSerializers,\
    EstoqueSerializers
from rest_framework import status
from Produto.models import Produto



# Create your views here.
class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializers
    permission_classes = [permissions.IsAuthenticated]


class MovimentacaoViewSet(viewsets.ModelViewSet):
    queryset = MOVIMENTACAO.objects.all()
    serializer_class = MovimentacaoSerializers
    permission_classes = [permissions.IsAuthenticated]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        item=self.preenchecampos(request)
        serializer = self.get_serializer(data=item)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.salvaestoque(request)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def preenchecampos(self,request):
        produto = Produto.objects.get(id=int(request.data['codigo']))
        dados = request.data.copy()
        nume = Item.objects.last()
        dados.__setitem__('descricao',produto.descricao)
        dados.__setitem__('codigo_interno', f'{produto.codigo} - {nume.id + 1}')
        return dados


    def salvaestoque(self,request):
        movimentacao = MOVIMENTACAO.objects.get(id=int(request.data['movimentacao']))
        produto = Produto.objects.get(id=int(request.data['codigo']))
        estoque = Estoque.objects.filter(posicao=movimentacao.posicao, produto=produto)
        if movimentacao.tipo == '1':#Entrada
             if not estoque:
                 try:
                   Estoque.objects.create(posicao=movimentacao.posicao, produto=produto,
                                        quantidade=float(request.data['quantidade']))
                 except:
                     raise ValidationError('Não foi possivel salvar Estoque')
             else:
                saldo = float(estoque[0].quantidade) + float(request.data['quantidade'])
                e = Estoque.objects.get(id=int(estoque[0].id))
                e.quantidade = saldo
                e.save()

        if movimentacao.tipo == '2': #Saida
            if float(request.data['quantidade']) > float(estoque[0].quantidade):
                raise ValidationError('Saldo insuficiente')
            else:
                saldo = float(estoque[0].quantidade) - float(request.data['quantidade'])
                e = Estoque.objects.get(id=int(estoque[0].id))
                e.quantidade = saldo
                e.save()



class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializers
    permission_classes = [permissions.IsAuthenticated]


class PosicaoViewSet(viewsets.ModelViewSet):
    queryset = Posicao.objects.all()
    serializer_class = PosicaoSerializers
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # substituir nome
        posicao = request.data.copy()
        unidade = Unidade.objects.get(id=int(posicao['unidade']))
        posicao.__setitem__('nome',f'{unidade} - {request.data["rua"]}{request.data["predio"]}'\
                          f'{request.data["nivel"]}{request.data["sequencia"]}')

        serializer = self.get_serializer(data=posicao)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)