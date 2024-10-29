from django.db import models
from cloudinary.models import CloudinaryField
from authentication.models import UserModel


# modelo para las categorias
class CategoryModel(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  status = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'
    db_table = 'categories'

  def __str__(self):
      return self.get_name_display()


# modelo para las propiedades
class HoldingModel(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200)
  description = models.TextField()
  address = models.CharField(max_length=100)
  image = CloudinaryField('image')
  price = models.FloatField()
  bedr = models.IntegerField()
  bath = models.IntegerField()
  park = models.IntegerField()
  STATUS_CHOICES = (
    ('ACTIVE', 'Activo'),
    ('INACTIVE', 'Inactivo'),
    ('DELETED', 'Eliminado'),
  )
  status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  category = models.ForeignKey(
    CategoryModel, 
    on_delete=models.CASCADE,
    related_name='holdings',
    db_column='category_id'
  )

  class Meta:
    verbose_name = 'Propiedad'
    verbose_name_plural = 'Propiedades'
    db_table = 'holdings'
  

# Modelo para los logs de creacion y actulizacion de datos de las propiedades
class UpdateHoldingLogModel(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(
    UserModel,
    on_delete=models.CASCADE,
    related_name='update_user_logs',
    db_column='user_id',
  )
  holding = models.ForeignKey(
    HoldingModel,
    on_delete=models.CASCADE,
    related_name='update_holding_logs',
    db_column='holding_id',
  )
  field = models.CharField(max_length=100)
  value = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = 'Log de actualizacion'
    verbose_name_plural = 'Logs de actualizacion'
    db_table = 'update_holding_logs'
    
