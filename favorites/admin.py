from django.contrib import admin
from .models import Favorite


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('user__username', 'movie__title')
    readonly_fields = ('created_at',)
