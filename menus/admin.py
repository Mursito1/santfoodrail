from django.contrib import admin

from .models import Calificacion, Calificacion_Menu, Ingrediente, Ingrediente_menu, Menu

# Register your models here.
admin.site.register(Menu)
admin.site.register(Ingrediente)
admin.site.register(Ingrediente_menu)
admin.site.register(Calificacion)
admin.site.register(Calificacion_Menu)