from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_line, name="post_line"),
    path('posts/<int:pk>/', views.post_details, name="post_details"),
]
