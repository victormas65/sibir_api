from django.urls import path

from tipoinformacion.views import CreateTipoInformacionView, ListTipoInformacionView
from .views import *  # Esto importa todas las vistas desde views.py

urlpatterns = [
    # Vistas para TipoInformacion
    path('tipos-informacion/', ListTipoInformacionView.as_view(), name='list_tipo_informacion'),
    path('tipos-informacion/create/', CreateTipoInformacionView.as_view(), name='create_tipo_informacion'),
    
    # Vistas para Contacto
    path('contactos/', ListContactoView.as_view(), name='list_contactos'),
    path('contactos/<int:pk>/', DetailContactoView.as_view(), name='detail_contacto'),
    path('contactos/create/', CreateContactoView.as_view(), name='create_contacto'),
    path('contactos/update/<int:pk>/', UpdateContactoView.as_view(), name='update_contacto'),
    path('contactos/delete/<int:pk>/', DeleteContactoView.as_view(), name='delete_contacto'),
]
