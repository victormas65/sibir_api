# views.py
from rest_framework import generics, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import TipoInformacion
from .serializers import TipoInformacionSerializer

TIPO_INFORMACION_TAG = 'Tipos de Información'

class ListTipoInformacionView(generics.ListAPIView):
    queryset = TipoInformacion.objects.all()
    serializer_class = TipoInformacionSerializer

    @swagger_auto_schema(tags=[TIPO_INFORMACION_TAG])
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return Response({
            'message': 'Tipos de información listados exitosamente',
            'data': response.data
        }, status=status.HTTP_200_OK)

class CreateTipoInformacionView(generics.CreateAPIView):
    serializer_class = TipoInformacionSerializer

    @swagger_auto_schema(tags=[TIPO_INFORMACION_TAG])
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            'message': 'Tipo de información creado exitosamente',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
