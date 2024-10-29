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

  class Meta:
    model = PostModel
    fields = '__all__'
