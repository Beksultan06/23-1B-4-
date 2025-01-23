from django.urls import path
from app.blog.views import blog

urlpatterns = [
    path("blog/", blog, name="blog")
]
