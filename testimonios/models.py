from django.db import models

class Testimonio(models.Model):
    id = models.AutoField(primary_key=True)
    comentario = models.TextField()
    autor = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Testimonio'
        verbose_name_plural = 'Testimonios'
        db_table = 'testimonios'

    def __str__(self):
        return f"{self.autor}: {self.comentario[:50]}"
