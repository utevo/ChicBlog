from django.contrib import admin
from django.urls import path, include

from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView,
    )


app_name = 'chicblog'

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),
         name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),
         name='post_delete'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('about/', views.about, name='about')
]
