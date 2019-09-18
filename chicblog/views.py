from django.shortcuts import render
from .models import Post

def home(request):
    all_posts = Post.objects.all()
    context = { 
        'posts': all_posts
    }
    return render(request, 'chicblog/home.html', context)


def about(request):
    return render(request, 'chicblog/about.html')

