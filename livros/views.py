from django.shortcuts import render, redirect, get_object_or_404

from .forms import LivroForm
from .models import Livro


def index(request):
    livros = Livro.objects.all()
    return render(request, 'livros/index.html', {'livros': livros})


def detail(request, pk):
    livros = get_object_or_404(Livro, pk=pk)
    return render(request, 'livros/detail.html', {'livros': livros})


def add(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('livros:index')
    else:
        form = LivroForm()

    return render(request, 'livros/add.html',
                  {'form': form})


def edit(request, pk):
    livros = get_object_or_404(Livro, pk=pk)

    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livros)

        if form.is_valid():
            form.save()

            return redirect('livros:index')
    else:
        form = LivroForm(instance=livros)
    return render(request, 'livros/edit.html', {'form': form})


def delete(request, pk):
    livros = get_object_or_404(Livro, pk=pk)
    livros.delete()

    return redirect('livros:index')
