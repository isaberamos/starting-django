from django.contrib import admin
from galeria.models import Fotografia

class ListaFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)

# Registro do BD no admin
admin.site.register(Fotografia, ListaFotografias)