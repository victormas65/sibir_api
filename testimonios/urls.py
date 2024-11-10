# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('testimonios/', ListTestimonioView.as_view(), name='list_testimonios'),
    path('testimonios/<int:pk>/', DetailTestimonioView.as_view(), name='detail_testimonio'),
    path('testimonios/create/', CreateTestimonioView.as_view(), name='create_testimonio'),
    path('testimonios/update/<int:pk>/', UpdateTestimonioView.as_view(), name='update_testimonio'),
    path('testimonios/delete/<int:pk>/', DeleteTestimonioView.as_view(), name='delete_testimonio'),
]
