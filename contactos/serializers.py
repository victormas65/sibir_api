from rest_framework import serializers
from .models import Contacto, TipoInformacion

class ContactoSerializer(serializers.ModelSerializer):
    # Asume que 'tipoinformacion' es una clave foránea en el modelo Contacto
    tipoinformacion = serializers.PrimaryKeyRelatedField(queryset=TipoInformacion.objects.all())

    class Meta:
        model = Contacto
        fields = ['id', 'nombres', 'telefono', 'email', 'mensaje', 'precio', 'fecha', 'hora', 'tipoinformacion']

    # Opcional: hacer campos específicos como 'precio' y 'hora' opcionales
    precio = serializers.DecimalField(max_digits=10, decimal_places=2, required=False, allow_null=True)
    hora = serializers.IntegerField(required=False, allow_null=True)
