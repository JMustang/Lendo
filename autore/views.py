from django.shortcuts import render

from .forms import AutorForm

def  index(request):
    return render(request, 'autor/index.html')

def add(request):

    form = AutorForm()
    return render(request, 'autor/add.html', {'form': form})