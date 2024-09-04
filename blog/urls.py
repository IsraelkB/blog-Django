from django.urls import path
from . import views

from blog import views
from .views import post_detail

urlpatterns = [
    path("", views.home, name="home_page"),
    path("posts", views.posts, name="posts_page"),
    path("posts/<slug:slug>", views.post_detail, name="post_detail")
]
