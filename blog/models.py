from django.db import models
from publication.models import HoldingModel

# Modelo para los clientes
class CustomerModel(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    document_number = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    STATUS_CHOICES = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
        ('DELETED', 'Eliminado'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVO')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'customers'

    def __str__(self):
        return f"{self.first_name} {self.last_name} - <{self.email}>"

    # Método para obtener el nombre completo
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

# Modelo para los Post del Blog
class PostModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    STATUS_CHOICES = (
        ('PENDING', 'Pendiente'),
        ('VALIDADO', 'Validado'),
        ('DELETED', 'Eliminado'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(
        CustomerModel, 
        on_delete=models.CASCADE,
        related_name='posts',
        db_column='customer_id'
    )
    holding = models.ForeignKey(
        HoldingModel, 
        on_delete=models.CASCADE,
        related_name='holding',
        db_column='holding_id'
    )

    class Meta:
        verbose_name = 'Post del Blog'
        verbose_name_plural = 'Posts del Blog'
        db_table = 'posts'
