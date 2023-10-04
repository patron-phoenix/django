from django.contrib import admin

from .models import Usuario
from .models import Libro
from .models import Ejemplar
from .models import Autor


# class AutorAdmin(admin.ModelAdmin):
#     list_display=("nombre")

class LibroAdmin(admin.ModelAdmin):
    list_display=("titulo","editorial")
    search_fields=["titulo","editorial"]

class EjemplarAdmin(admin.ModelAdmin):
    list_display=("localizacion","libro")
    #search_fields=["localizacion"]

class UsuarioAdmin(admin.ModelAdmin):
    list_display=("nombre","telefono","direccion")
    search_fields=["nombre"]



admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Libro,LibroAdmin)
#admin.site.register(Ejemplar)
admin.site.register(Ejemplar,EjemplarAdmin)
admin.site.register(Autor)
#admin.site.register(Autor,AutorAdmin)
