from rest_framework import serializers
from .models import PostModel, CustomerModel, HoldingModel

class PostSerializer(serializers.ModelSerializer):
    # Campo de solo lectura para obtener el nombre completo del cliente
    customer_name = serializers.CharField(source='customer.get_full_name', read_only=True)
    
    # Otros campos
    status = serializers.CharField(read_only=True)  # Campo de solo lectura
    customer = serializers.PrimaryKeyRelatedField(queryset=CustomerModel.objects.all())  # Devuelve solo el ID de customer
    holding = serializers.PrimaryKeyRelatedField(queryset=HoldingModel.objects.all())  # Devuelve solo el ID de holding

    class Meta:
        model = PostModel
        fields = [
            'id',  # ID del post
            'title',  # Título
            'description',  # Descripción
            'status',  # Estado (solo lectura)
            'customer',  # ID del cliente (customer_id)
            'holding',  # ID de la holding (holding_id)
            'customer_name',  # Nombre del cliente
            'created_at',  # Fecha de creación
        ]
