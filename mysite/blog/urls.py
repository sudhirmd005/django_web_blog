from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_line, name="post_line"),
    path('posts/<int:pk>/', views.post_details, name="post_details"),
    path('posts/new/', views.post_new, name='post_new'),
    path('posts/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
