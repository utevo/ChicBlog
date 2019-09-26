from django.contrib import admin
from django.urls import path, include

from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView
    )


app_name = 'chicblog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('about/', views.about, name='about')
]
