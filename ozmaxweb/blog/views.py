from django.shortcuts import render

from .models import Post, Category


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    context = {'posts': posts, 'categories': categories}
    tmpl = 'blog/home.html'
    return render(request, tmpl, context)


def single_post(request, slug):
    post = Post.objects.get(slug=slug)
    categories = Category.objects.all()
    context = {'post': post, 'categories': categories}
    tmpl = 'blog/single.html'
    return render(request, tmpl, context)
