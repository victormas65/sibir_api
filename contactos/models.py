from django.db import models
from tipoinformacion.models import TipoInformacion  # Importar el modelo de TipoInformacion

class Contacto(models.Model):
    nombres = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telefono = models.CharField(max_length=255)
    mensaje = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Permite null
    fecha = models.DateTimeField()
    hora = models.IntegerField(null=True, blank=True)  # Permite null
    
    # Clave foránea a TipoInformacion
    tipoinformacion = models.ForeignKey(TipoInformacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombres
