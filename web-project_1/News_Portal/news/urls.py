from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostsDetail.as_view())
]