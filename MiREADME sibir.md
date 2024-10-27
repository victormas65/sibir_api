# Django SIBIR

   python -m venv entorno_venv
   entorno_venv/bin/activate
   deactivate

   pip install -r requirements.txt


## cadena de conexion para tu BD
    crea bd Postgres en blanco: "django_sibir"
    actualiza datos de conexion en ".env"
    

## git ignore
    https://www.toptal.com/developers/gitignore 


   python manage.py runserver

```





// -------------------------------------------------------
//                     Proyecto SIBIR
//--------------------------------------------------------

# eCommerce

cadena de conexion para BD en render


``` Terminales
 pip install django
 pip install django-cors-headers            # para manejar los headers
 pip install djangorestframework            # para el swagger
 pip install djangorestframework-simplejwt
 pip install -U drf-yasg                     # para 
 pip install psycopg2-binary                 # para el postgres
 pip install PyJWT                           # para el JWT
 pip install python-dotenv    
 pip install pytz                            # para el timezone
 pip install PyYAML                          # para el yaml
 pip install sqlparse                       # para el sql
 pip install uritemplate
 pip install cloudinary
 pip install requests


 pip install Django djangorestframework python-dotenv psycopg2-binary django-cors-headers djangorestframework-simplejwt drf-yasq 

 ```

 ```Error 
 #si aparece el siguiente error: NO MODULE NAMED "PKG_RESOURCES"
 pip install -U setuptools



 ``` settings.py
 INSTALLED_APPS = [
    ...,
    "rest_framework",
    "drf_yasg",
    "corsheaders",
    "rest_framework_simplejwt",
```


1.- importar user del modulo de autentication


2.- importar manager del modulo de autentication


3.- models
4.- serializers
5.- views
6.- urls


7.- agrega ruta en include global

Incluye swagger en la url principal
  - copian 3 bloques de codigo: IMPORTE, SCHEMA_VIEW y PATH's


   # crear un superusuario
       python manage.py createsuperuser
           username: admin
           email: admin@gmail.com
           password: adminadmin

   # ejecutar el servidor
       python manage.py runserver
           http://127.0.0.1:8000/swagger/
           

# datos de conexion en la B

postgresql://django_ecommerce_db_vjbx_user:3olF9O9Mj6grJtO2mre7PAfMBYdhOjmz@dpg-cscr95bv2p9s73fmakrg-a.oregon-postgres.render.com/django_ecommerce_db_vjbx


NUBEFACT

https://www.nubefact.com/api_tokens
DICCIONARIO: https://docs.google.com/document/d/1QWWSILBbjd4MDkJl7vCkL2RZvkPh0IC7Wa67BvoYIhA/edit?tab=t.0 

API='https://api.nubefact.com/api/v1/3bd67239-c07b-479b-a060-800def37e479'
TOKEN='29e284846dad423bb9b87c76b2a1be127222cafab77d410ba66efac011ec8f15'
