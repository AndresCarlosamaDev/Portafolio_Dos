from django.db import models

# Create your models here.
class Proyecto(models.Model):
    imagen = models.ImageField(upload_to='Proyecto/imagen')
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        nombreProyecto = 'Proyecto: ' + self.titulo
        return nombreProyecto
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    mensaje = models.TextField()
    
    def __str__(self) -> str:
        nombreContacto = 'Nombre: ' + self.nombre
        return nombreContacto