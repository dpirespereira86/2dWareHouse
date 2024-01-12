from django.db import models

# Create your models here.
class Familia(models.Model):
    nome= models.CharField(max_length=30)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Familia"


class Produto(models.Model):

    ATIVO_CHOICES = (
        ("Sim", "Sim"),
        ("Não", "Nao")
    )

    UNIDADE_CHOICE =(
        ("Cj","Conjunto"),("Cx", "Caixa"),("Dz", "Dúzia"),("Fd", "Fardo"),
        ("Fl", "Folha"),("Gl", "Galão"), ("Lt", "Lote"),("Jg", "Jogo"),
        ("Kg", "Kilograma"),("L", "Litro"),("Lta", "Lata"),("M", "Metro"),
        ("Mil", "Milheiro"),("Par", "Par"),("Pct", "Pacote"),("Pç", "Peça"),
        ("Res", "Resma"),("Rl", "Rolo"),("Ton", "Tonelada"),("Und","Unidade"),
        ("Vd", "Vidro"),("M³","Metro_cubico"),("M²","Metro_quadrado"),
    )

    id= models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=30,null=False,blank='False',unique=True)
    codigo_Aaxiliar = models.CharField(max_length=30,null=False,blank='False',unique=True)
    descricao = models.CharField(max_length=100,null=False,blank='False')
    familia= models.ForeignKey(Familia,on_delete=models.CASCADE)
    unidade = models.CharField(max_length=30,choices=UNIDADE_CHOICE,null=False,blank='False')
    tipo_item = models.CharField(max_length=30,null=False,blank='False')
    ativo = models.CharField(max_length=30,choices=ATIVO_CHOICES,null=False,blank='False')
    especificacao = models.CharField(max_length=200,default='')
    fornecedor = models.CharField(max_length=200, null=True, blank='True')
    observacao = models.CharField(max_length=200,default='')
    imagem= models.ImageField(default='')
    tempo_validade = models.IntegerField(default=0)
    comprimento = models.DecimalField(max_digits=6,decimal_places=2,default=0.00)
    largura= models.DecimalField(max_digits=6,decimal_places=2,default=0.00)
    altura = models.DecimalField(max_digits=6,decimal_places=2,default=0.00)
    prazo_frete= models.DecimalField(max_digits=6,decimal_places=2,default=0.00)
    peso = models.DecimalField(max_digits=6,decimal_places=2,default=0.00)
    saldo = models.DecimalField(max_digits=6, decimal_places=2,default=0.00)
    estoque_minimo = models.DecimalField(max_digits=6,decimal_places=2,default=0.00)
    estoque_maximo = models.DecimalField(max_digits=6,decimal_places=2,default=0.00)
    estoque_seguranca = models.DecimalField(max_digits=6,decimal_places=2,default=0.00)


    def __str__(self):
        return f'{self.codigo}'

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"



# Create your models here.
