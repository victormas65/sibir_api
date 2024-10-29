from django.urls import path
from .views import *

urlpatterns = [
  path('posts/create', CreatePostView.as_view()),
  path('posts/list', ListPostView.as_view()),

]
