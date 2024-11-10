# serializers.py

from rest_framework import serializers
from .models import Testimonio

class TestimonioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonio
        fields = ['id', 'comentario', 'autor']
