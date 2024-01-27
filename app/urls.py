
from django.contrib import admin
from django.urls import path,  include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autor/', include('autore.urls')),
    path('livros/', include('livros.urls')),
    path('', include('core.urls')),
]
