from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Menu(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        app_label = 'calificaciones'
        
    def __str__(self):
        return self.nombre
    
class Review(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    calificacion = models.PositiveSmallIntegerField()
    comentario = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.menu.nombre} - {self.calificacion}'