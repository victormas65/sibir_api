# tipoinformacion/models.py

from django.db import models

class TipoInformacion(models.Model):
    name = models.CharField(max_length=255)
    flg_status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
