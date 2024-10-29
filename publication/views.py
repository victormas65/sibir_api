from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import (
  MultiPartParser,
  FormParser,
)
from utils.pagination import Pagination
from rest_framework.pagination import PageNumberPagination
from django.http import Http404
from .models import (
  CategoryModel,
  HoldingModel,
)
from .serializers import (
  CategorySerializer,
  HoldingSerializer,
)
from drf_yasg.utils import swagger_auto_schema        # schema para el swagger
from drf_yasg import openapi
from authentication.permissions import (
  IsAuthenticated,
  IsAdmin,
  IsSellerOrAdmin
)

CATEGORY_TAG = 'Categoria de Propiedades'
HOLDING_TAG = 'Propiedades'


#------------------------------------------------------------------------------
###                       CRUD PARA CATEGORIAS                              ###
# ----------------------------------------------------------------------------- 

# Lista de categorias
class ListCategoryView(generics.ListAPIView):
  queryset = CategoryModel.objects.all()
  serializer_class = CategorySerializer

  @swagger_auto_schema(tags=[ CATEGORY_TAG ])
  def get(self, request, *args, **kwargs):
    """ Lista de Categorias: metodo get """
    response = super().get(request, *args, **kwargs)
    return Response({
      'message': 'Categorias listadas exitosamente',
      'data': response.data
    }, status=status.HTTP_200_OK
  )

# Crea una nueva categoria
class CreateCategoryView(generics.CreateAPIView):
  serializer_class = CategorySerializer
  permission_classes = [IsAuthenticated, IsAdmin]

  @swagger_auto_schema(tags=[ CATEGORY_TAG ])
  def post(self, request, *args, **kwargs):
    """ Crea una nueva categoria: metodo post """
    response = super().post(request, *args, **kwargs)
    return Response({
      'message': 'Categoria creada exitosamente',
      'data': response.data
      }, status=status.HTTP_201_CREATED
  )

# Actualiza una categoria
class UpdateCategoryView(generics.UpdateAPIView):
  queryset = CategoryModel.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [IsAuthenticated, IsAdmin]

  @swagger_auto_schema(tags=[ CATEGORY_TAG ])
  def put(self, request, *args, **kwargs):
    """ Actualiza una categoria: metodo put """
    try:
      response = super().put(request, *args, **kwargs)
      return Response({
        'message': 'Categoria actualizada exitosamente',
        'data': response.data
        }, status=status.HTTP_200_OK
      )
    except Http404:
      return Response({
        'message': 'Categoria no encontrada',
        }, status=status.HTTP_404_NOT_FOUND)

  @swagger_auto_schema(tags=[ CATEGORY_TAG ])
  def patch(self, request, *args, **kwargs):
    """ Actualiza una categoria: metodo patch """
    try:
      response = super().partial_update(request, *args, **kwargs)
      return Response({
        'message': 'Categoria actualizada exitosamente',
        'data': response.data
        }, status=status.HTTP_200_OK)
    except Http404:
      return Response({
        'message': 'Categoria no encontrada',
        }, status=status.HTTP_404_NOT_FOUND)

# Elimina una categoria
class DeleteCategoryView(generics.DestroyAPIView):
  queryset = CategoryModel.objects.all()
  permission_classes = [IsAuthenticated, IsAdmin]

  @swagger_auto_schema(tags=[ CATEGORY_TAG ])
  def delete(self, request, *args, **kwargs):
    """ Elimina una categoria: metodo delete """
    try:
      category = self.get_object()
      category.status = False
      category.save()
      return Response({
        'message': 'Categoria eliminada exitosamente',
        }, status=status.HTTP_200_OK)
    except Http404:
      return Response({
        'message': 'Categoria no encontrada',
        }, status=status.HTTP_404_NOT_FOUND)


#------------------------------------------------------------------------------
###                             HOLDINGS                                    ###
# ----------------------------------------------------------------------------- 
  
# Lista de holdings
class ListHoldingView(generics.ListAPIView):
  #queryset = HoldingModel.objects.all()   no es necesario porque se filtra en la funcion get_queryset
  queryset = HoldingModel.objects.all()
  serializer_class = HoldingSerializer
  pagination_class = Pagination
  permission_classes = [IsAuthenticated, IsSellerOrAdmin]

  @swagger_auto_schema(tags=[ HOLDING_TAG ])
  def get(self, request, *args, **kwargs):
    """ Lista de propiedades: metodo get """
    response = super().get(request, *args, **kwargs)

    return Response({
      'message': 'Propiedades listadas exitosamente',
      'data': response.data['results'],
      'count': response.data['count'],
      'next': response.data['next'],
      'previous': response.data['previous']
      }, status=status.HTTP_200_OK)

# Lista de propiedades activas (activos)
class ListActiveHoldingView(generics.ListAPIView):
  serializer_class = HoldingSerializer
  pagination_class = Pagination

  def get_queryset(self):
    queryset = HoldingModel.objects.filter(status='ACTIVE').order_by('name')
    return queryset
  
  @swagger_auto_schema(tags=[ HOLDING_TAG ])
  def get(self, request, *args, **kwargs):
    """ Lista de propiedades activas: metodo get """
    response = super().get(request, *args, **kwargs)
    return Response({
      'message': 'Propiedades listadas exitosamente',
      'data': response.data['results'],
      'count': response.data['count'],
      'next': response.data['next'],
      'previous': response.data['previous']
      }, status=status.HTTP_200_OK)
  
# Busca propiedades por nombre
class SearchHoldingView(generics.ListAPIView):
  serializer_class = HoldingSerializer
  pagination_class = Pagination

  def get_queryset(self):
    queryset = HoldingModel.objects.filter(name__icontains=self.kwargs['name']).order_by('-id')
    return queryset

  @swagger_auto_schema(tags=[ HOLDING_TAG ])
  def get(self, request, *args, **kwargs):
    """ Buscar propiedades por el nombre: metodo get """
    response = super().get(request, *args, **kwargs)

    return Response({
      'message': 'Propiedades listadas exitosamente',
      'data': response.data['results'],
      'count': response.data['count'],
      'next': response.data['next'],
      'previous': response.data['previous']
      }, status=status.HTTP_200_OK) 

# Crea una propiedad
class CreateHoldingView(generics.CreateAPIView):
  serializer_class = HoldingSerializer
  #permission_classes = [IsAuthenticated, IsAdmin]
  parser_classes = [MultiPartParser, FormParser]

  # Parametro para subir desde SWAGER la imagen de la propiedad (formuDATA) 
  image_param = openapi.Parameter(
    'image',
    openapi.IN_FORM,
    type=openapi.TYPE_FILE,
    required=True,
    description='Imagen de la propiedad'
  )

  @swagger_auto_schema(
    tags=[ HOLDING_TAG ],
    manual_parameters=[ image_param ],
    consumes=['multipart/form-data']
  )
  def post(self, request, *args, **kwargs):
    """ Crea una propiedad: metodo post """
    response = super().post(request, *args, **kwargs)
    return Response({
      'message': 'Propiedad creada exitosamente',
      'data': response.data
      }, status=status.HTTP_201_CREATED)

# Actualiza una propiedad
class UpdateHoldingView(generics.UpdateAPIView):
  queryset = HoldingModel.objects.all()
  serializer_class = HoldingSerializer
#  permission_classes = [IsAuthenticated, IsAdmin]
  parser_classes = [MultiPartParser, FormParser]

  # Parametro para subir desde SWAGER la imagen de la propiedad (formuDATA) 
  name_param = openapi.Parameter(
    'name',
    openapi.IN_FORM,
    type=openapi.TYPE_STRING,
    required=False,
    description='Nombre de la propiedad'
  )
  image_param = openapi.Parameter(
    'image',
    openapi.IN_FORM,
    type=openapi.TYPE_FILE,
    required=False,
    description='Imagen de la propiedad'
  )

  @swagger_auto_schema(
      tags=[ HOLDING_TAG ],
      manual_parameters=[ image_param ],
      consumes=['multipart/form-data']
    )
  def put(self, request, *args, **kwargs):
    """ Actualiza una propiedad: metodo put """
    try:
      response = super().put(request, *args, **kwargs)
      return Response({
        'message': 'Propiedad actualizada exitosamente',
        'data': response.data
        }, status=status.HTTP_200_OK
      )
    except Http404:
      return Response({
        'message': 'Propiedad no encontrado',
        }, status=status.HTTP_404_NOT_FOUND)
  
  @swagger_auto_schema(
      tags=[ HOLDING_TAG ],
      manual_parameters=[ name_param, image_param ],
      consumes=['multipart/form-data']
  )
  def patch(self, request, *args, **kwargs):
    """ Actualiza una propiedad: metodo patch """
    try:
      response = super().partial_update(request, *args, **kwargs)
      return Response({
        'message': 'Propiedad actualizado exitosamente',
        'data': response.data
        }, status=status.HTTP_200_OK)
    except Http404:
      return Response({
        'message': 'Propiedad no encontrado',
        }, status=status.HTTP_404_NOT_FOUND)
    
# Elimina una propiedad
class DeleteHoldingView(generics.DestroyAPIView):
  queryset = HoldingModel.objects.all()
#  permission_classes = [IsAuthenticated, IsAdmin]

  @swagger_auto_schema(tags=[ HOLDING_TAG ])
  def delete(self, request, *args, **kwargs):
    """ Elimina una propiedad: metodo delete """
    try:
      holding = self.get_object()
      holding.status = 'DELETED'
      holding.save()
      return Response({
        'message': 'Propiedad eliminada exitosamente',
        }, status=status.HTTP_200_OK)
    except Http404:
      return Response({
        'message': 'Propiedad no encontrada',
        }, status=status.HTTP_404_NOT_FOUND) 

