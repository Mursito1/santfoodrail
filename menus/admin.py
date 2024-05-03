from django.contrib import admin

from .models import Ingrediente, Ingrediente_menu, Menu

# Register your models here.
admin.site.register(Menu)
admin.site.register(Ingrediente)
admin.site.register(Ingrediente_menu)
