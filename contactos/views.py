# contacto/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.http import Http404
from .models import Contacto, TipoInformacion
from .serializers import ContactoSerializer

CONTACTO_TAG = 'Contactos'

class ListContactoView(generics.ListAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

    @swagger_auto_schema(tags=[CONTACTO_TAG])
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return Response({
            'message': 'Contactos listados exitosamente',
            'data': response.data
        }, status=status.HTTP_200_OK)

class DetailContactoView(generics.RetrieveAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

    @swagger_auto_schema(tags=[CONTACTO_TAG])
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return Response({
            'message': 'Contacto encontrado exitosamente',
            'data': response.data
        }, status=status.HTTP_200_OK)

class CreateContactoView(generics.CreateAPIView):
    serializer_class = ContactoSerializer

    @swagger_auto_schema(tags=[CONTACTO_TAG])
    def post(self, request, *args, **kwargs):
        # Asegúrate de que se pase un ID válido para 'tipoinformacion'
        tipoinformacion_id = request.data.get('tipoinformacion')

        # Verifica que el 'id' de 'tipoinformacion' sea válido
        try:
            tipoinformacion = TipoInformacion.objects.get(id=tipoinformacion_id)
        except TipoInformacion.DoesNotExist:
            return Response({
                'message': 'Tipo de información no encontrado'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Ahora, pasa el 'tipoinformacion' como ID en los datos para crear el contacto
        data = request.data
        data['tipoinformacion'] = tipoinformacion.id

        # Creación del Contacto con el ID de TipoInformacion
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response({
            'message': 'Contacto creado exitosamente',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

class UpdateContactoView(generics.UpdateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

    @swagger_auto_schema(tags=[CONTACTO_TAG])
    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'message': 'Contacto actualizado exitosamente',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class DeleteContactoView(generics.DestroyAPIView):
    queryset = Contacto.objects.all()

    @swagger_auto_schema(tags=[CONTACTO_TAG])
    def delete(self, request, *args, **kwargs):
        try:
            contacto = self.get_object()
            contacto.delete()
            return Response({
                'message': 'Contacto eliminado exitosamente',
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Contacto no encontrado',
            }, status=status.HTTP_404_NOT_FOUND)
