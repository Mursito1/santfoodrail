from django.db import models

# Create your models here.
class Contacto(models.Model):
    mensaje_contacto = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title