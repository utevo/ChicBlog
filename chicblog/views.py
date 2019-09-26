from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'chicblog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'chicblog/post_detail.html'
    context_object_name = 'post'


def about(request):
    return render(request, 'chicblog/about.html')
