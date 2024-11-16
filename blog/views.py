from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import PostModel
from rest_framework.serializers import ValidationError
from drf_yasg.utils import swagger_auto_schema
from django.db import transaction

# Registra el Post del Blog
class CreatePostView(generics.CreateAPIView):
    serializer_class = PostSerializer

    @swagger_auto_schema(tags=['Posts del Blog'])
    def post(self, request, *args, **kwargs):
        """ Crear un Post del Blog (método POST) """
        try:
            # Usamos el serializer para validar y guardar el objeto
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                post = serializer.save()  # Guarda el post en la base de datos

                # Personalizar la respuesta con todos los datos esperados
                return Response({
                    'id': post.id,  # ID generado automáticamente
                    'holdingid': post.holdingid,  # URL de imagen simulada
                    'titulo': post.title,  # Título
                    'autor': post.customer.first_name + " " + post.customer.last_name,  # Nombre completo del autor
                    'descripcion': post.description,  # Descripción
                    'fecha': post.created_at.strftime('%Y-%m-%d %H:%M:%S'),  # Fecha formateada
                    'status': post.status,  # Estado
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'message': 'Datos inválidos',
                    'errors': serializer.errors,
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'message': 'Error al crear el post del blog',
                'errors': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Listar los post del blog
class ListPostView(generics.ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    
    @swagger_auto_schema(tags=['Posts del Blog'])
    def get(self, request, *args, **kwargs):
        """ Listar post del blog (método GET) """
        response = super().get(request, *args, **kwargs)
        
        return Response({
            'message': 'Listado de post del blog exitosamente',
            'data': response.data
        }, status=status.HTTP_200_OK)
