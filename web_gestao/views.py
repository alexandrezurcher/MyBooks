from django.shortcuts import render,redirect,HttpResponse 
from .models import Book
from.forms import BookForm


def livros(request):
    dados = {
        'dados': Book.objects.all()
    }
    return render(request,'livros/livros.html',context=dados)

def details(request, id_livro):
    dados = {
       'dados': Book.objects.get(pk=id_livro)
    }
    return render(request,'livros/details.html',dados)

def criar(request):
    if request.method =='POST':
        livro_form = BookForm(request.POST)
        if livro_form.is_valid():
            livro_form.save()
        return redirect('livros')
    else:
        livro_form = BookForm()
        formulario = {
            'formulario': livro_form
        }
        return render(request, 'livros/novo_livro.html',context=formulario)
    
def editar(request, id_livro):
    livro = Book.objects.get(pk=id_livro)
    if request.method =='GET':
        formulario = BookForm(instance = livro)
        return render(request,'livros/novo_livro.html', {'formulario': formulario})
    #caso requisicao seja POST
    else:
       formulario = BookForm(request.POST,instance=livro)
       if formulario.is_valid():
           formulario.save()
       return redirect('livros')    

def excluir(request,id_livro):
    book = Book.objects.get(pk=id_livro)
    if request.method == 'POST':
        book.delete()
        return redirect('livros')
    return render(request, 'livros/confirmar_exclusao.html',{'item': book})