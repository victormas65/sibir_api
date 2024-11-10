# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('propiedades/list', ListPropiedadView.as_view(), name='list-propiedad'),
    path('propiedades/<int:pk>', DetailPropiedadView.as_view(), name='detail-propiedad'),
    path('propiedades/create', CreatePropiedadView.as_view(), name='create-propiedad'),
    path('propiedades/update/<int:pk>', UpdatePropiedadView.as_view(), name='update-propiedad'),
    path('propiedades/delete/<int:pk>', DeletePropiedadView.as_view(), name='delete-propiedad'),
]
