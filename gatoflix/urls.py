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
