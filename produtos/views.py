from django.shortcuts import render, redirect
from .forms import CategoriaForm, FornecedorForm, ProdutoForm

# Create your views here.



def home(request):
    return render(request, 'home.html')


def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('sucesso')  # Redireciona após sucesso
    else:
        form = CategoriaForm()
    return render(request, 'cadastrar_categoria.html', {'form': form})

def cadastrar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('sucesso')
    else:
        form = FornecedorForm()
    return render(request, 'cadastrar_fornecedor.html', {'form': form})

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
           # return redirect('sucesso')
    else:
        form = ProdutoForm()
    return render(request, 'cadastrar_produto.html', {'form': form})
