from django.db import models
from django.urls import reverse

class Banda(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    origen = models.CharField(max_length=100, blank=True, null=True)
    foto = models.ImageField(upload_to='bandas/', blank=True, null=True)
    fecha_formacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('banda-list')

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    lanzamiento = models.DateField()
    genero = models.CharField(max_length=50, blank=True, null=True)
    portada = models.ImageField(upload_to='albumes/', blank=True, null=True)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='albumes')
    descripcion = models.TextField(blank=True, null=True)
    duracion_total = models.DurationField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.banda.nombre}"
    
        
    def get_absolute_url(self):
        return reverse('album-list')
    
    
class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    duracion = models.TimeField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='canciones')
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='canciones')
    foto = models.ImageField(upload_to='canciones/', blank=True, null=True)  # Campo para la foto de la canción
    fecha_lanzamiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.album.titulo} - {self.banda.nombre}"
    
    def get_absolute_url(self):
        return reverse('cancion-list')
