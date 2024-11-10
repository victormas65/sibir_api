# views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import Http404
from .models import Propiedad
from .serializers import PropiedadSerializer
from authentication.permissions import IsAuthenticated, IsAdmin

PROP_TAG = 'Propiedades2'

class ListPropiedadView(generics.ListAPIView):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializer

    @swagger_auto_schema(tags=[PROP_TAG])
    def get(self, request, *args, **kwargs):
        """ Lista de propiedades: metodo GET """
        response = super().get(request, *args, **kwargs)
        return Response({
            'message': 'Propiedades listadas exitosamente',
            'data': response.data
        }, status=status.HTTP_200_OK)

class DetailPropiedadView(generics.RetrieveAPIView):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializer

    @swagger_auto_schema(tags=[PROP_TAG])
    def get(self, request, *args, **kwargs):
        """ Obtener detalles de una propiedad: metodo GET """
        response = super().get(request, *args, **kwargs)
        return Response({
            'message': 'Propiedad encontrada exitosamente',
            'data': response.data
        }, status=status.HTTP_200_OK)

class CreatePropiedadView(generics.CreateAPIView):
    serializer_class = PropiedadSerializer
    parser_classes = [MultiPartParser, FormParser]

    image_param = openapi.Parameter(
        'imagen',
        openapi.IN_FORM,
        type=openapi.TYPE_FILE,
        required=True,
        description='Imagen de la propiedad'
    )

    @swagger_auto_schema(
        tags=[PROP_TAG],
        manual_parameters=[image_param],
        consumes=['multipart/form-data']
    )
    def post(self, request, *args, **kwargs):
        """ Crea una nueva propiedad: metodo POST """
        response = super().post(request, *args, **kwargs)
        return Response({
            'message': 'Propiedad creada exitosamente',
            'data': response.data
        }, status=status.HTTP_201_CREATED)

class UpdatePropiedadView(generics.UpdateAPIView):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializer
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(tags=[PROP_TAG])
    def put(self, request, *args, **kwargs):
        """ Actualiza una propiedad: metodo PUT """
        try:
            response = super().put(request, *args, **kwargs)
            return Response({
                'message': 'Propiedad actualizada exitosamente',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Propiedad no encontrada',
            }, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(tags=[PROP_TAG])
    def patch(self, request, *args, **kwargs):
        """ Actualiza parcialmente una propiedad: metodo PATCH """
        try:
            response = super().partial_update(request, *args, **kwargs)
            return Response({
                'message': 'Propiedad actualizada exitosamente',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Propiedad no encontrada',
            }, status=status.HTTP_404_NOT_FOUND)

class DeletePropiedadView(generics.DestroyAPIView):
    queryset = Propiedad.objects.all()

    @swagger_auto_schema(tags=[PROP_TAG])
    def delete(self, request, *args, **kwargs):
        """ Elimina una propiedad: metodo DELETE """
        try:
            propiedad = self.get_object()
            propiedad.status = 'DELETED'  # Cambiar el estado a "eliminado"
            propiedad.save()
            return Response({
                'message': 'Propiedad eliminada exitosamente',
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Propiedad no encontrada',
            }, status=status.HTTP_404_NOT_FOUND)
