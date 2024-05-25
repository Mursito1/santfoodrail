from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "tipo_contacto", "mensaje_contacto"]


class ContactoAdminForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ["estado_contacto"]

    def __init__(self, *args, **kwargs):
        super(ContactoAdminForm, self).__init__(*args, **kwargs)
        # Hacer que los demás campos solo sean de lectura
        for field in self.fields:
            if field != 'estado_contacto':
                self.fields[field].widget.attrs['readonly'] = True