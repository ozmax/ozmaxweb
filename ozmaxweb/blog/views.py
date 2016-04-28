from django.shortcuts import render

from .models import Post


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts': posts}
    tmpl = 'blog/home.html'
    return render(request, tmpl, context)


def single_post(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    tmpl = 'blog/single.html'
    return render(request, tmpl, context)
