from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager

# Modelo para los roles de usuario
class RoleModel(models.Model):
    id = models.AutoField(primary_key=True)
    ROL_CHOICES = (
        ('ADMIN', 'Administrador'),
        ('SELLER', 'Vendedor'),
        ('CUSTOMER', 'Cliente'),
    )
    name = models.CharField(max_length=10, choices=ROL_CHOICES, default='SELLER', unique=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        db_table = 'roles'

    def __str__(self):
        return self.get_name_display()


# Modelo para los usuarios
class UserModel(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  
    role = models.ForeignKey(
        RoleModel, 
        on_delete=models.SET_NULL,
        related_name='users',
        db_column='role_id',
        null=True,
        blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'users'

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"