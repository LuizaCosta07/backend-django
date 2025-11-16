from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Count


class GatoFlixAdminBase(admin.ModelAdmin):
    """Base admin class com customizações GatoFlix."""
    
    class Media:
        css = {
            'all': ('admin/css/gatoflix.css',)
        }


@admin.register
def admin_site_customize():
    """Customize Django admin site."""
    admin.site.site_header = "GatoFlix Admin 🐾"
    admin.site.site_title = "GatoFlix"
    admin.site.index_title = "Bem-vindo ao GatoFlix"
