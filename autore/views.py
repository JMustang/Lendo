from django.shortcuts import render, redirect, get_object_or_404

from .forms import AutorForm
from .models import Autor


def index(request):
    autores = Autor.objects.all()
    return render(request, 'autor/index.html', {
        'autores': autores,
    })


def detail(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'autor/detail.html', {
        'autor': autor,
    })

def add(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autor:index')
    else:
        form = AutorForm()
    return render(request, 'autor/add.html', {'form': form})
