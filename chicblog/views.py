from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    )

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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'chicblog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'chicblog/about.html')
