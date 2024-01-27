from django.db import models

from autore.models import Autor


class Livro(models.Model):
    WANTED = 'wanted'
    WAITTING = 'waiting'
    READING = 'reading'
    READ = 'read'

    STATUS_CHOICES = [
        (WANTED, 'Quero ler'),
        (WAITTING, 'Aguardando'),
        (READING, 'Lendo'),
        (READ, 'Lido'),
    ]

    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, related_name='livros', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=WAITTING)
