from rest_framework import serializers
from .models import (
  CategoryModel,
  HoldingModel,
)

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = CategoryModel
    fields = '__all__'

class HoldingSerializer(serializers.ModelSerializer):
  class Meta:
    model = HoldingModel
    fields = '__all__'

  def to_representation(self, instance):
    representation = super().to_representation(instance)
    representation['image'] = instance.image.url
    return representation
    

    
  