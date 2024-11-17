from django.urls import path
from .views import *

urlpatterns = [
  path('categories/list', ListCategoryView.as_view()),
  path('categories/create', CreateCategoryView.as_view()),
  path('categories/update/<int:pk>', UpdateCategoryView.as_view()),
  path('categories/delete/<int:pk>', DeleteCategoryView.as_view()),
  
  path('holdings/list', ListHoldingView.as_view()),
  path('holdings/list/active', ListActiveHoldingView.as_view()),
  path('holdings/search/<str:name>', SearchHoldingView.as_view()),
  path('holdings/create', CreateHoldingView.as_view()),
  path('holdings/update/<int:pk>', UpdateHoldingView.as_view()),
  path('holdings/delete/<int:pk>', DeleteHoldingView.as_view()),
  path('holdings/<int:id>/', ListHoldingView.as_view(), name='holding_detail'),
]