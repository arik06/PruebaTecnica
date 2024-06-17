from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio =  models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True, )
    categoria = models.CharField(max_length=50)
    modelo =  models.CharField(max_length=50)
    año = models.IntegerField()
    imagen_url = models.URLField()
    
    def __str__(self):
        return self.nombre