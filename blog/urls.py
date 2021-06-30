from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('blogs', views.blogs),
    path('blogs/<int:id>', views.blog_detail, name='blog_detail'),
]