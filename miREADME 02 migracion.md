# Django Rest Framework

## Instalación
```bash
  pip install Django                # Framework
  pip install djangorestframework   # API
  pip install python-dotenv         # Variables de entorno
  pip install psycopg2-binary       # Base de datos
```

creacion del proyecto
```bash
  django-admin startproject django_rest_framework .
```

## Configuración
```python: settings.py
  INSTALLED_APPS = [
    "...",
    "rest_framework",
    "..."
  ]
  ```

### Variables de entorno
Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```bash: .env
DB_NAME=django_rest_framework
DB_USER=postgres
DB_PASSWORD=root
DB_HOST=localhost
DB_PORT=5432
```

### Base de datos en Django
```python: settings.py
import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
```

1. crear la aplicacion
2. registrar la aplicacion
3. crear el modelo
4. hacer la migracion

5. crear el serializer.py

se crean los views.py
```python: views.py
    from rest_framework import generics, status
    from rest_framework.response import Response
    from .models import ProductCategoryModel
    from .serilizers import ProductCategorySerializer

    class ProductCategoryView(generics.ListAPIView):
```
Ver video 10/10/ desde las 9:30 pm


```modulo/urls.py

```

```app/urls.py
    from django.urls import path, include

    urlpatterns = [
        path("admin/", admin.site.urls),
        path('api/', include('almacen.urls')),
```

```app/views.py

```
