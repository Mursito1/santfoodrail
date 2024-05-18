from django import forms
from django.contrib.auth.forms import UserCreationForm
from menus.models import Menu

class CustomUserCreationForm(UserCreationForm):
    pass 

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'