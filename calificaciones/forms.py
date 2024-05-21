from django import forms 
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['calificacion', 'comentario']
        widgets = {
            'calificacion': forms.NumberInput(attrs={'min':1, 'max':5}),
            'comentario': forms.Textarea(attrs={'rows':4}),
        }