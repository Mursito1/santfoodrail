from django.contrib import admin

from .models import Calificacion, Calificacion_Menu, Ingrediente, Menu, Proteina, Salsa, Vegetal

# Register your models here.
admin.site.register(Menu)
admin.site.register(Ingrediente)
admin.site.register(Calificacion)
admin.site.register(Calificacion_Menu)
admin.site.register(Vegetal)
admin.site.register(Proteina)
admin.site.register(Salsa)