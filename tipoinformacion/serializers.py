# serializers.py
from rest_framework import serializers
from .models import TipoInformacion

class TipoInformacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInformacion
        fields = ['id', 'name', 'flg_status']
