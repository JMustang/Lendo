from django.shortcuts import render, redirect

from .forms import LivroForm
from .models import Livro


def index(request):
    livros = Livro.objects.all()
    return render(request, 'livros/index.html', {'livros': livros})


def add(request):
    if request.method =='POST':
        form = LivroForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('livros:index')
    else:
        form = LivroForm()

    return render(request, 'livros/add.html',
                  {'form': form})

