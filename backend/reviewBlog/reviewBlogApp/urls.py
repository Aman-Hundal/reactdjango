from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("posts", views.posts, name="posts" ),
  path("posts/create", views.posts_create, name="posts_create" )
]