# views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import Http404
from .models import Testimonio
from .serializers import TestimonioSerializer
from authentication.permissions import IsAuthenticated, IsAdmin

TESTIMONIO_TAG = 'Testimonios'

class ListTestimonioView(generics.ListAPIView):
    queryset = Testimonio.objects.all()
    serializer_class = TestimonioSerializer

    @swagger_auto_schema(tags=[TESTIMONIO_TAG])
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return Response({
            'message': 'Testimonios listados exitosamente',
            'data': response.data
        }, status=status.HTTP_200_OK)

class DetailTestimonioView(generics.RetrieveAPIView):
    queryset = Testimonio.objects.all()
    serializer_class = TestimonioSerializer

    @swagger_auto_schema(tags=[TESTIMONIO_TAG])
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return Response({
            'message': 'Testimonio encontrado exitosamente',
            'data': response.data
        }, status=status.HTTP_200_OK)

class CreateTestimonioView(generics.CreateAPIView):
    serializer_class = TestimonioSerializer
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(tags=[TESTIMONIO_TAG])
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({
            'message': 'Testimonio creado exitosamente',
            'data': response.data
        }, status=status.HTTP_201_CREATED)

class UpdateTestimonioView(generics.UpdateAPIView):
    queryset = Testimonio.objects.all()
    serializer_class = TestimonioSerializer

    @swagger_auto_schema(tags=[TESTIMONIO_TAG])
    def put(self, request, *args, **kwargs):
        try:
            response = super().put(request, *args, **kwargs)
            return Response({
                'message': 'Testimonio actualizado exitosamente',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Testimonio no encontrado',
            }, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(tags=[TESTIMONIO_TAG])
    def patch(self, request, *args, **kwargs):
        try:
            response = super().partial_update(request, *args, **kwargs)
            return Response({
                'message': 'Testimonio actualizado parcialmente',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Testimonio no encontrado',
            }, status=status.HTTP_404_NOT_FOUND)

class DeleteTestimonioView(generics.DestroyAPIView):
    queryset = Testimonio.objects.all()

    @swagger_auto_schema(tags=[TESTIMONIO_TAG])
    def delete(self, request, *args, **kwargs):
        try:
            testimonio = self.get_object()
            testimonio.delete()
            return Response({
                'message': 'Testimonio eliminado exitosamente',
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Testimonio no encontrado',
            }, status=status.HTTP_404_NOT_FOUND)
