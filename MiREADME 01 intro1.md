# Django Intro

## Instalación
```bash
   # crear entorno virtual
      python -m venv nombre_env
      source nombre_env/bin/activate

   pip install Django

       pip freeze > requirements.txt
```

## Crear un proyecto
```bash
   django-admin startproject nombre_proyecto .

   # migraciones
   python manage.py makemigrations   # Nuestras propias migraciones
   python manage.py makemigrations nombre_aplicacionde_la_aplicacion # migraciones de django
   python manage.py migrate          # migracion en sqllite   
   python manage.py showmigrations   # listar migraciones

   # crear un superusuario
       python manage.py createsuperuser
           username: admin
           email: admin@gmail.com
           password: adminadmin
```

## Migraciones
```bash
    # migraciones
    python manage.py makemigrations   # Nuestras propias migraciones
    python manage.py makemigrations nombre_aplicacionde_la_aplicacion # migraciones de django
    python manage.py migrate          # migracion en sqllite   
    python manage.py showmigrations   # listar migraciones

   https://sqliteonline.com/ 
```

## ejecutar el servidor
```bash
   python manage.py runserver
   # navegar  
   http://127.0.0.1:8000/admin/
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


## crear un modelo
```bash
   # se crean los modelos de la nueva aplicacion
   # se realizan las migraciones
   code models.py
   python manage.py makemigrations nombre_nueva_aplicacion
   python manage.py migrate
```