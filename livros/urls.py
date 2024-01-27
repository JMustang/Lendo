from django.urls import path

from . import views

app_name = 'livros'

urlpatterns = [
    path('add/', views.add, name='add'),
]