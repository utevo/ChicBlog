from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
    )
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
    )
from django.contrib.auth.models import User

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'chicblog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6


class UserPostListView(ListView):
    model = Post
    template_name = 'chicblog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return user.post_set.order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'chicblog/post_detail.html'
    context_object_name = 'post'


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'chicblog/post_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if post.author == self.request.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'chicblog/post_confirm_delete.html'
    context_object_name = 'post'
    success_url = '/'

    def test_func(self):
        post = self.get_object()

        if post.author == self.request.user:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'chicblog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'chicblog/about.html')
