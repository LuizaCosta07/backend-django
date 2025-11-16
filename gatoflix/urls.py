"""
URL configuration for gatoflix project.
"""

from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "GatoFlix Admin 🐾"
admin.site.site_title = "GatoFlix"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('movies/', include('movies.urls')),
    path('favorites/', include('favorites.urls')),
]

from django.contrib.auth.models import User
from django.http import HttpResponse

def create_luiza(request):
    if not User.objects.filter(username='luiza').exists():
        User.objects.create_superuser('luiza', 'luiza@gatoflix.com', 'luiza')
        return HttpResponse("Usuário 'luiza' criado com sucesso!")
    return HttpResponse("Usuário 'luiza' já existe.")


urlpatterns += [
    path('create-luiza/', create_luiza),
]
