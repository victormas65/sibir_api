from rest_framework import serializers
from .models import (
  PostModel,
  CustomerModel,
)

class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomerModel
    fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    customer = serializers.SerializerMethodField()

    class Meta:
        model = PostModel
        fields = '__all__'

    def get_customer(self, obj):
        """ Devuelve el nombre completo del cliente en lugar de solo el ID """
        if obj.customer:
            return f"{obj.customer.first_name} {obj.customer.last_name}"
        return None