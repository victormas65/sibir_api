# tipoinformacion/urls.py

from django.urls import path
from .views import ListTipoInformacionView, CreateTipoInformacionView

urlpatterns = [
    path('tipos-informacion/', ListTipoInformacionView.as_view(), name='list_tipo_informacion'),
    path('tipos-informacion/create/', CreateTipoInformacionView.as_view(), name='create_tipo_informacion'),
]
