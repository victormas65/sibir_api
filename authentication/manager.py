from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    # Creando el usuario
    def create_user(self, email, password=None, role=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Datos adicionales para el super usuario
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        # # Obtén el rol de administrador (asumiendo que tiene id=1)
        # try:
        #     admin_role = self.RoleModel.objects.get(id=1)  
        # except self.RoleModel.DoesNotExist:
        #     raise ValueError("El rol (1)Administrador, no existe en la base de datos.")
        # # Asigna el rol de administrador al superusuario
        # extra_fields['role'] = admin_role 

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')

        return self.create_user(email, password, **extra_fields)

