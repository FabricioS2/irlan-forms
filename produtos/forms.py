from django import forms
from .models import Categoria, Fornecedor, Produto
from django.core.exceptions import ValidationError
import re

#from .models import Question

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['Nome', 'Classe', 'Descricao']
        widgets = {
            'Descricao': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
        }

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['Nome', 'Distancia', 'Descricao']
        widgets = {
            'Descricao': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['Nome', 'Codigo_do_produto', 'Descricao', 'Preco', 'Quantidade_em_estoque', 'Categorias', 'Fornecedores']
        widgets = {
            'Descricao': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
            'Categorias': forms.CheckboxSelectMultiple(),
        }

    def clean_Preco(self):
        preco_text = self.cleaned_data["Preco"]
        if preco_text < 2:
            raise ValidationError("preço tem que ter mais de 2 digitos!!!")
        return preco_text

    def clean_Quantidade_em_estoque(self):
        estoque_text = self.cleaned_data["Quantidade_em_estoque"]
        if not (estoque_text >= 0):
            raise ValidationError("A quantidade em estoque deve ser um número inteiro maior ou igual a zero.!!!")
        return estoque_text

    def clean_Codigo_do_produto(self):
        Codigo_do_produto_text = self.cleaned_data["Codigo_do_produto"]
        if not re.match(r'^[a-zA-Z0-9]+$', Codigo_do_produto_text):
            raise ValidationError('O código do produto deve conter apenas letras e números, sem espaços ou caracteres especiais.')
        return Codigo_do_produto_text

    def clean_Nome(self):
        nome_text = self.cleaned_data["Nome"]
        if len(nome_text) < 3:
            raise ValidationError("produto deve ter pelo menos 3 caracteres.!!!")
        return nome_text
