from django.contrib import admin
from .models import Produto,Fornecedor,Categoria
# Register your models here


class ProdutoAdmin(admin.ModelAdmin):
   list_display = ['Nome', 'Codigo_do_produto',"Descricao","Preco","Quantidade_em_estoque","Data_de_criacao"] #listagem de atributos
   list_filter = ['Data_de_criacao'] #atributos a serem utilizados como filtros
   search_fields = ['Nome',"Codigo_do_produto"] #atributos a serem utilizados em buscas
   ordering = ['-Data_de_criacao'] #ordenação a partir de um atributo

class FornecedortoAdmin(admin.ModelAdmin):
   list_display = ['Nome', 'Distancia',"Descricao"] #listagem de atributos
   list_filter = ['Nome'] #atributos a serem utilizados como filtros
   search_fields = ['Nome'] #atributos a serem utilizados em buscas

class CategoriatoAdmin(admin.ModelAdmin):
   list_display = ['Nome', 'Classe',"Descricao"] #listagem de atributos
   list_filter = ['Nome'] #atributos a serem utilizados como filtros
   search_fields = ['Nome'] #atributos a serem utilizados em buscas


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Fornecedor, FornecedortoAdmin)
admin.site.register(Categoria, CategoriatoAdmin)



