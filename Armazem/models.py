from django.db import models
from Produto.models import Produto

# Create your models here.
class Unidade(models.Model):
    nome= models.CharField(max_length=30,unique=True)

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = "Unidade"
        verbose_name_plural = "Unidades"


class Posicao(models.Model):

    ALFABETO_CHOICE = (
        ("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"),
        ("E", "E"), ("F", "F"), ("G", "G"), ("H", "H"),
        ("I", "I"), ("J", "J"), ("K", "K"), ("L", "L"),
        ("M", "M"), ("N", "N"), ("O", "O"), ("P", "P"),
        ("Q", "Q"), ("R", "R"), ("S", "S"), ("T", "T"),
        ("U", "U"), ("V", "V"), ("W", "W"),("X", "X"),("Y", "Y"),
        ("Z", "Z")
    )

    NUMERO_CHOICE = (
        ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"),
        ("5", "5"), ("6", "6"), ("7", "7"), ("8", "8"),
        ("9", "9"), ("10", "10"), ("11", "11"), ("12", "13"),
        ("14", "14"), ("15", "15"), ("16", "16"), ("17", "17"),
        ("18", "18"), ("19", "19"), ("20", "20"), ("21", "22"),
        ("23", "23"), ("24", "24"), ("25", "25"), ("26", "26"), ("27", "27"),
        ("28", "28")
    )

    id = models.AutoField(primary_key=True)
    unidade=models.ForeignKey(Unidade,related_name='posicoes',on_delete=models.CASCADE)
    nome = models.CharField(max_length=30,)
    rua = models.CharField(max_length=30,choices=ALFABETO_CHOICE,null=False,blank=False)
    predio = models.CharField(max_length=30,choices=ALFABETO_CHOICE,null=False,blank=False)
    nivel = models.CharField(max_length=30,choices=NUMERO_CHOICE,null=False,blank=False)
    sequencia = models.CharField(max_length=30,choices=NUMERO_CHOICE,null=False,blank=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Posição"
        verbose_name_plural="Posições"

class MOVIMENTACAO(models.Model):
    MOVIMENTACAO_CHOICE = (('1', 'Entrada'), ('2', 'Saida'),)

    id = models.AutoField(primary_key=True, unique=True)
    tipo = models.CharField(max_length=30, choices=MOVIMENTACAO_CHOICE, null=False, blank=False)
    date=models.DateField()
    operador= models.CharField(max_length=30)
    posicao= models.ForeignKey(Posicao,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tipo}'

    class Meta:
        verbose_name = "Movimentaçao"
        verbose_name_plural="Movimentações"


class Item(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    codigo=models.ForeignKey(Produto,related_name='itens',on_delete=models.CASCADE)
    codigo_interno = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    quantidade = models.DecimalField(max_digits=5,decimal_places=2)
    movimentacao = models.ForeignKey(MOVIMENTACAO,related_name='itens',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.codigo}'

    class Meta:
        verbose_name = "Item"
        verbose_name_plural="Itens"


class Estoque(models.Model):
    posicao = models.ForeignKey(Posicao,on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto,related_name='estoques',on_delete=models.CASCADE)
    quantidade=models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return f'{self.posicao.nome}'

    class Meta:
        verbose_name = "Estoque"
        verbose_name_plural = "Estoques"