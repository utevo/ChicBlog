from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
    )
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
    )
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import Http404
from django.http.response import HttpResponseRedirect

from .models import Post, Comment
from .forms import CommentCreateForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = context['post']
        context['comments'] = post.comment_set.all()
        
        context['comment_create_form'] = CommentCreateForm()

        return context


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


def comment_create(request, pk):
    if request.method == 'GET':
        raise Http404
    else:
        comment_form = CommentCreateForm(request.POST)
        comment_form.instance.author = request.user
        comment_form.instance.post = Post.objects.get(pk=pk)

        if comment_form.is_valid():
            comment_form.save()
            return HttpResponseRedirect(reverse('chicblog:post_detail', kwargs={'pk': pk}))
            
        else:
            raise Http404



def about(request):
    return render(request, 'chicblog/about.html')
