from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "tipo_contacto", "mensaje_contacto"]


class ContactoAdminForm(forms.ModelForm):
    respuesta = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Contacto
        fields = ["estado_contacto", "respuesta"] 

    def __init__(self, *args, **kwargs):
        super(ContactoAdminForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'estado_contacto':
                self.fields[field].widget.attrs['readonly'] = True