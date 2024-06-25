from django.contrib import admin

from .models import Menu, Proteina, Salsa, Vegetal

# Register your models here.
admin.site.register(Menu)
admin.site.register(Vegetal)
admin.site.register(Proteina)
admin.site.register(Salsa)