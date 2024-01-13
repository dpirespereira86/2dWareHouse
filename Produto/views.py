from rest_framework.response import Response

from .models import Produto,Familia
from .serializers import ProdutoSerializers,FamiliaSerializers,ProdutoEstoqueSerializers
from rest_framework import viewsets
from rest_framework import permissions
from Armazem.models import Estoque
from Armazem.serializers import EstoqueSerializers

# Create your views here.
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializers
    permission_classes = [permissions.IsAuthenticated]


class ProdutoEstoqueViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoEstoqueSerializers
    permission_classes = [permissions.IsAuthenticated]


class FamiliaViewSet(viewsets.ModelViewSet):
    queryset = Familia.objects.all()
    serializer_class = FamiliaSerializers
    permission_classes = [permissions.IsAuthenticated]

