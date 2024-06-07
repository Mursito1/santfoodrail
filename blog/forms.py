from django import forms
from django.contrib.auth.forms import UserCreationForm
from menus.models import Menu, Proteina, Salsa, Vegetal

class CustomUserCreationForm(UserCreationForm):
    pass 

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {
            'proteina': forms.CheckboxSelectMultiple,
            'vegetal': forms.CheckboxSelectMultiple,
            'salsa': forms.CheckboxSelectMultiple,
        }
        