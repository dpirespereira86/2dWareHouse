from django.http import HttpRequest
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Produto,Familia
from .serializers import ProdutoSerializers,FamiliaSerializers
from rest_framework import status

# Create your views here.
class ProdutoApiView(APIView):
    """
    Comentário da API
    """

    def get(self,request):
       print(request.user)
       produtos = Produto.objects.all()
       serializer = ProdutoSerializers(produtos,many=True)
       return Response(serializer.data)

    def post(self,request):
        serializer=ProdutoSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FamiliaApiView(APIView):
    """
    Comentário da API
    """

    def get(self, request):
        familias = Familia.objects.all()
        serializer = FamiliaSerializers(familias, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=FamiliaSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)