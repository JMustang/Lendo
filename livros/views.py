from django.shortcuts import render, redirect

from .forms import LivroForm

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

