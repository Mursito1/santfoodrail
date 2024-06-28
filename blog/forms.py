import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from menus.models import Menu, Proteina, Salsa, Vegetal
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_id = self.instance.id if self.instance else None 
        
        if User.objects.exclude(id=user_id).filter(email=email).exists():
            raise forms.ValidationError('Este email ya está en uso. Por favor, elige otro.')
        
        return email
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if not re.match(r'^[A-Za-zñÑ]{1,15}$', first_name):
            raise forms.ValidationError('El nombre debe contener solo letras, máximo 15 caracteres y sin espacios.')

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if not re.match(r'^[A-Za-zñÑ ]{1,30}$', last_name):
            raise forms.ValidationError('Los apellidos debe contener solo letras y espacios, máximo 30 caracteres.')

        return last_name
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if not re.match(r'^[A-Za-zñÑ]{1,15}$', username):
            raise forms.ValidationError('El username debe contener solo letras, máximo 15 caracteres y sin espacios.')

        return username

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email', max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {
            'proteina': forms.CheckboxSelectMultiple,
            'vegetal': forms.CheckboxSelectMultiple,
            'salsa': forms.CheckboxSelectMultiple,
            'categoria': forms.CheckboxSelectMultiple,
        }

class ProteinaForm(forms.ModelForm):
    class Meta:
        model = Proteina
        fields = ['nombre']

class SalsaForm(forms.ModelForm):
    class Meta:
        model = Salsa
        fields = ['nombre']

class VegetalForm(forms.ModelForm):
    class Meta:
        model = Vegetal
        fields = ['nombre']
        