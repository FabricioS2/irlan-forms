from django.db import models

# Create your models here.

class Categoria(models.Model):
    Nome = models.CharField("Nome da categoria",max_length=200,blank=False, null=False)
    Classe = models.CharField("Classe",max_length=1, blank=False, null=False)
    Descricao = models.CharField("Descrição",max_length=900,blank=True)

    def __str__(self):
       return self.Nome

class Fornecedor(models.Model):
    Nome = models.CharField("Nome do fornecedor",max_length=200,blank=False, null=False)
    Distancia = models.DecimalField("Distancia",max_digits=10, decimal_places=3)
    Descricao = models.CharField("Descrição",max_length=900,blank=True)

    def __str__(self):
       return self.Nome


class Produto(models.Model):
    Nome = models.CharField("Nome do produto",max_length=200,blank=False, null=False)
    Codigo_do_produto = models.CharField("Código do produto",max_length=200, unique=True, blank=False, null=False)
    Descricao = models.CharField("Descrição",max_length=900,blank=True)
    Preco = models.DecimalField("Preço",max_digits=10, decimal_places=2)
    Quantidade_em_estoque = models.DecimalField("Quantidade em estoque",decimal_places=0,max_digits=5)
    Data_de_criacao = models.DateField("Data de criação", auto_now_add=True)
    Categorias = models.ManyToManyField(Categoria)
    Fornecedores = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
       return self.Nome

