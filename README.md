# SIBIR API con Django Rest Framework, Swagger, Cloudinary y Postgres

## Instalación
```bash
   # crear entorno virtual
      python -m venv nombre_env
      source nombre_env/bin/activate

       pip install -r requirements.txt
```

## Crear un proyecto
```bash
   django-admin startproject nombre_proyecto .

   # migraciones
   python manage.py makemigrations authentication    # migracion de authentication
   python manage.py makemigrations publication       # migracion de publication
   python manage.py migrate                          # ejecuta migraciones 
   python manage.py showmigrations                   # listar migraciones

   # crear un superusuario
       python manage.py createsuperuser
          email: admin@gmail.com
          First Name: admin
          Last Name: V+
          password: adminadmin
          Password (again): adminadmin
```


## crear una aplicacion
```bash
    python manage.py startapp nombre_aplicacion

    ## se registra en settings.py
    INSTALLED_APPS = [
        "......",
        "almacen",
        "nombre_nueva_aplicacion",
    ]
```


### Instalacion de UNFOLD
        ```bash
        pip install django-unfold

        ```python: settings.py
        INSTALLED_APPS = [
            "unfold",  # before ``django.contrib.admin``
            "unfold.contrib.filters",  # optional, if special filters are needed
            "unfold.contrib.forms",  # optional, if special form elements are needed
            "unfold.contrib.inlines",  # optional, if special inlines are needed
            "unfold.contrib.import_export",  # optional, if django-import-export package is used
            "unfold.contrib.guardian",  # optional, if django-guardian package is used
            "unfold.contrib.simple_history",  # optional, if django-simple-history package is used

        ]
        ```

### 10. Registrar un modelo en mi admin de Django

        ```py
        # Esto es para unfold
                from django.contrib import admin
                from unfold.admin import ModelAdmin

                @admin.register(MiModel)
                class CustomAdminClass(ModelAdmin):
                    pass


        # Esto es para Django normal o Jazzmine
                from django.contrib import admin
                from .models import CategoriasModel, MiModel

                @admin.register(CategoriasModel)
                class CategoriasAdmin(admin.ModelAdmin):
                list_display =  ["nombre"]

                @admin.register(MiModel)
                class MiAdmin(admin.ModelAdmin):
                list_display = ["titulo", "stock", "contenido"]
        ```


## Ejecutar el servidor
```bash
   python manage.py runserver
   # navegar  
   - http://127.0.0.1:8000/admin/
   - http://127.0.0.1:8000/swagger/
```
