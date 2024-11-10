# Generated by Django 5.1.2 on 2024-11-10 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('mensaje', models.TextField()),
                ('tipoinformacion', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipocontacto', models.CharField(choices=[('VENDEDOR', 'Vendedor'), ('COMPRADOR', 'Comprador')], max_length=10)),
                ('fecha', models.DateTimeField()),
                ('hora', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
                'db_table': 'contactos',
            },
        ),
    ]
