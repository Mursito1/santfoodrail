from django.db import models


# Create your models here.

class Ingrediente(models.Model):
    nombre_ingrediente = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_ingrediente

class Calificacion(models.Model):
    calificacion = models.IntegerField()

    def __str__(self):
        return self.calificacion

class Proteina(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Vegetal(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre

class Vegetal1(Vegetal):
    pass

class Vegetal2(Vegetal):
    pass

class Vegetal3(Vegetal):
    pass

class Vegetal4(Vegetal):
    pass

class Vegetal5(Vegetal):
    pass
    
class Salsa(models.Model):
    nombre_salsa = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Menu(models.Model):
    nombre_menu = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    ganancia = models.PositiveIntegerField()
    estado_menu = models.BooleanField()
    descripcion_menu = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='images/')
    proteina = models.ForeignKey(Proteina, on_delete=models.PROTECT)
    vegetal1 = models.ForeignKey(Vegetal1, on_delete=models.PROTECT)
    vegetal2 = models.ForeignKey(Vegetal2, on_delete=models.PROTECT)
    vegetal3 = models.ForeignKey(Vegetal3, on_delete=models.PROTECT)
    vegetal4 = models.ForeignKey(Vegetal4, on_delete=models.PROTECT)
    vegetal5 = models.ForeignKey(Vegetal5, on_delete=models.PROTECT)
    salsa = models.ForeignKey(Salsa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_menu
    
    def promedio_calificacion(self):
        calificaciones = self.calificacion_menu_set.all()
        if calificaciones.exists():
            promedio = calificaciones.aggregate(models.Avg('calificacion__calificacion'))['calificacion__calificacion__avg']
            return round(promedio, 2)
        return 0.0
    
class Calificacion_Menu(models.Model):
    id_menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
    id_calificacion = models.ForeignKey(Calificacion, on_delete=models.PROTECT, null=True)

    def int(self):
        return self.id

class Ingrediente_menu(models.Model):
    id_ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT)
    id_menu = models.ForeignKey(Menu, on_delete=models.PROTECT)

    def __str__(self):
        return f'El menú "{self.id_menu.nombre_menu}" contiene el ingrediente "{self.id_ingrediente.nombre_ingrediente}".'
    

    
