from django.contrib import admin
from .models import Contacto, Estado_contacto, Tipo_contacto

# Register your models here.
admin.site.register(Contacto)
admin.site.register(Tipo_contacto)
admin.site.register(Estado_contacto)