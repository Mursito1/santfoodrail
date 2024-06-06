from django.contrib import admin

from .models import Calificacion, Calificacion_Menu, Ingrediente, Ingrediente_menu, Menu, Proteina, Salsa, Vegetal, Vegetal1, Vegetal2, Vegetal3, Vegetal4, Vegetal5

# Register your models here.
admin.site.register(Menu)
admin.site.register(Ingrediente)
admin.site.register(Ingrediente_menu)
admin.site.register(Calificacion)
admin.site.register(Calificacion_Menu)
admin.site.register(Vegetal)
admin.site.register(Vegetal1)
admin.site.register(Vegetal2)
admin.site.register(Vegetal3)
admin.site.register(Vegetal4)
admin.site.register(Vegetal5)
admin.site.register(Proteina)
admin.site.register(Salsa)