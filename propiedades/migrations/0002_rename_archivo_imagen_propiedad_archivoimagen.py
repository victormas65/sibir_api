# Generated by Django 5.1.2 on 2024-11-12 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propiedad',
            old_name='archivo_imagen',
            new_name='archivoImagen',
        ),
    ]
