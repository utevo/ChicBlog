from django.contrib import admin
from django.urls import path, include

from . import views


app_name = 'chicblog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('about/', views.about, name='about')
]
