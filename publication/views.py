from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from utils.pagination import Pagination
from django.http import Http404
from .models import CategoryModel, HoldingModel
from .serializers import CategorySerializer, HoldingSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from authentication.permissions import IsAuthenticated, IsAdmin, IsSellerOrAdmin

CATEGORY_TAG = 'Categoria de Propiedades'
HOLDING_TAG = 'Propiedades'


#------------------------------------------------------------------------------ 
### CRUD PARA CATEGORIAS 
#------------------------------------------------------------------------------ 

class ListCategoryView(generics.ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    @swagger_auto_schema(tags=[CATEGORY_TAG])
    def get(self, request, *args, **kwargs):
        """ Lista de Categorias: metodo GET """
        response = super().get(request, *args, **kwargs)
        return Response({
            'message': 'Categorías listadas exitosamente',
            'data': response.data
        }, status=status.HTTP_200_OK)


class CreateCategoryView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    @swagger_auto_schema(tags=[CATEGORY_TAG])
    def post(self, request, *args, **kwargs):
        """ Crea una nueva categoria: metodo POST """
        response = super().post(request, *args, **kwargs)
        return Response({
            'message': 'Categoría creada exitosamente',
            'data': response.data
        }, status=status.HTTP_201_CREATED)

class UpdateCategoryView(generics.UpdateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    @swagger_auto_schema(tags=[CATEGORY_TAG])
    def put(self, request, *args, **kwargs):
        """ Actualiza una categoría: metodo PUT """
        try:
            response = super().put(request, *args, **kwargs)
            return Response({
                'message': 'Categoría actualizada exitosamente',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Categoría no encontrada',
            }, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(tags=[CATEGORY_TAG])
    def patch(self, request, *args, **kwargs):
        """ Actualiza parcialmente una categoría: metodo PATCH """
        try:
            response = super().partial_update(request, *args, **kwargs)
            return Response({
                'message': 'Categoría actualizada exitosamente',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Categoría no encontrada',
            }, status=status.HTTP_404_NOT_FOUND)


class DeleteCategoryView(generics.DestroyAPIView):
    queryset = CategoryModel.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]

    @swagger_auto_schema(tags=[CATEGORY_TAG])
    def delete(self, request, *args, **kwargs):
        """ Elimina una categoría: metodo DELETE """
        try:
            category = self.get_object()
            category.status = False  # Desactivar la categoría en lugar de eliminarla
            category.save()
            return Response({
                'message': 'Categoría eliminada exitosamente',
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Categoría no encontrada',
            }, status=status.HTTP_404_NOT_FOUND)


#------------------------------------------------------------------------------ 
### CRUD PARA HOLDINGS 
#------------------------------------------------------------------------------ 

class ListHoldingView(generics.ListAPIView):
    queryset = HoldingModel.objects.all()
    serializer_class = HoldingSerializer
    pagination_class = Pagination

    @swagger_auto_schema(tags=[HOLDING_TAG])
    def get(self, request, *args, **kwargs):
        """ Lista de propiedades: metodo GET """
        response = super().get(request, *args, **kwargs)
        return Response({
            'message': 'Propiedades listadas exitosamente',
            'data': response.data['results'],
            'count': response.data['count'],
            'next': response.data['next'],
            'previous': response.data['previous']
        }, status=status.HTTP_200_OK)

class HoldingDetailView(generics.RetrieveAPIView):
    queryset = HoldingModel.objects.all()
    serializer_class = HoldingSerializer
    lookup_field = 'id' 

class ListActiveHoldingView(generics.ListAPIView):
    serializer_class = HoldingSerializer
    pagination_class = Pagination

    def get_queryset(self):
        return HoldingModel.objects.filter(status='ACTIVE').order_by('name')

    @swagger_auto_schema(tags=[HOLDING_TAG])
    def get(self, request, *args, **kwargs):
        """ Lista de propiedades activas: metodo GET """
        response = super().get(request, *args, **kwargs)
        return Response({
            'message': 'Propiedades activas listadas exitosamente',
            'data': response.data['results'],
            'count': response.data['count'],
            'next': response.data['next'],
            'previous': response.data['previous']
        }, status=status.HTTP_200_OK)


class SearchHoldingView(generics.ListAPIView):
    serializer_class = HoldingSerializer
    pagination_class = Pagination

    def get_queryset(self):
        return HoldingModel.objects.filter(name__icontains=self.kwargs['name']).order_by('-id')

    @swagger_auto_schema(tags=[HOLDING_TAG])
    def get(self, request, *args, **kwargs):
        """ Buscar propiedades por nombre: metodo GET """
        response = super().get(request, *args, **kwargs)
        return Response({
            'message': 'Propiedades encontradas exitosamente',
            'data': response.data['results'],
            'count': response.data['count'],
            'next': response.data['next'],
            'previous': response.data['previous']
        }, status=status.HTTP_200_OK)


class CreateHoldingView(generics.CreateAPIView):
    serializer_class = HoldingSerializer
    parser_classes = [MultiPartParser, FormParser]

    image_param = openapi.Parameter(
        'image', openapi.IN_FORM, type=openapi.TYPE_FILE, required=True, description='Imagen de la propiedad'
    )

    @swagger_auto_schema(tags=[HOLDING_TAG], manual_parameters=[image_param], consumes=['multipart/form-data'])
    def post(self, request, *args, **kwargs):
        """ Crea una propiedad: metodo POST """
        response = super().post(request, *args, **kwargs)
        return Response({
            'message': 'Propiedad creada exitosamente',
            'data': response.data
        }, status=status.HTTP_201_CREATED)


class UpdateHoldingView(generics.UpdateAPIView):
    queryset = HoldingModel.objects.all()
    serializer_class = HoldingSerializer
    parser_classes = [MultiPartParser, FormParser]

    name_param = openapi.Parameter(
        'name', openapi.IN_FORM, type=openapi.TYPE_STRING, required=False, description='Nombre de la propiedad'
    )
    image_param = openapi.Parameter(
        'image', openapi.IN_FORM, type=openapi.TYPE_FILE, required=False, description='Imagen de la propiedad'
    )

    @swagger_auto_schema(tags=[HOLDING_TAG], manual_parameters=[image_param], consumes=['multipart/form-data'])
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

    @swagger_auto_schema(tags=[HOLDING_TAG], manual_parameters=[name_param, image_param], consumes=['multipart/form-data'])
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


class DeleteHoldingView(generics.DestroyAPIView):
    queryset = HoldingModel.objects.all()

    @swagger_auto_schema(tags=[HOLDING_TAG])
    def delete(self, request, *args, **kwargs):
        """ Elimina una propiedad: metodo DELETE """
        try:
            holding = self.get_object()
            holding.status = 'DELETED'  # Cambiar a "DELETED" en lugar de eliminarla completamente
            holding.save()
            return Response({
                'message': 'Propiedad eliminada exitosamente',
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Propiedad no encontrada',
            }, status=status.HTTP_404_NOT_FOUND)
