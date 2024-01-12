from .models import Produto,Familia
from .serializers import ProdutoSerializers,FamiliaSerializers
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializers
    permission_classes = [permissions.IsAuthenticated]


class FamiliaViewSet(viewsets.ModelViewSet):
    queryset = Familia.objects.all()
    serializer_class = FamiliaSerializers
    permission_classes = [permissions.IsAuthenticated]

