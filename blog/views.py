from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import (
  PostSerializer,
)
from .models import (
  PostModel,
)
from rest_framework.serializers import ValidationError
from drf_yasg.utils import swagger_auto_schema        # schema para el swagger
#from django.db import blog 


#------------------------------------------------------------------------------
###                  APIS PARA LOS POST DEL BLOG                            ###
# -----------------------------------------------------------------------------
POST_TAG = 'Posts del Blog'

# registra el Post del Blog
class CreatePostView(generics.CreateAPIView):
    serializer_class = PostSerializer

    @swagger_auto_schema(tags=[POST_TAG])
    def post(self, request, *args, **kwargs):
        """ Crear un Post del Blog (método POST) """
        try:
            with blog.atomic():
                response = super().post(request, *args, **kwargs)
                post_data = response.data

                return Response({
                    'message': 'Post del blog creado exitosamente',
                    'data': post_data
                }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'message': 'Error al crear el post del blog',
                'errors': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 

# Listar los post del blog 
class ListPostView(generics.ListAPIView):
   queryset = PostModel.objects.all()
   serializer_class = PostSerializer
   
   @swagger_auto_schema(tags=[POST_TAG])
   def get(self, request, *args, **kwargs):
      """ Listar post del blog (método GET) """
      response = super().get(request, *args, **kwargs)
      
      return Response({
        'message': 'Listado de post del blog exitosamente',
        'data': response.data
      }, status=status.HTTP_200_OK)


