from django import forms
from .models import Categoria, Fornecedor, Produto

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
