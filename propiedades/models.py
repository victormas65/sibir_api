from django.db import models
from cloudinary.models import CloudinaryField

class Propiedad(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to="imagenes")
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    nDormitorios = models.PositiveIntegerField(verbose_name="Número de Dormitorios")
    nSSHH = models.PositiveIntegerField(verbose_name="Número de SSHH")
    nCocheras = models.PositiveIntegerField(verbose_name="Número de Cocheras")
    direccion = models.CharField(max_length=300)
    archivoImagen = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Propiedades2'
        verbose_name_plural = 'Propiedades2'
        db_table = 'propiedades2'

    def __str__(self):
        return f"{self.titulo} - {self.direccion}"