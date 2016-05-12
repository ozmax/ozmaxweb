from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Category
from .blog_utils import get_archive

def home(request, tag=None):
    posts = Post.objects.all()
    archive = get_archive(posts)
    if tag:
        posts = Post.objects.filter(categories__name=tag)
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    categories = Category.objects.all()
    context = {'filter_tag': tag, 'posts': posts, 'categories': categories, 'archive': archive}
    tmpl = 'blog/home.html'
    return render(request, tmpl, context)


def single_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post = Post.objects.get(slug=slug)
    categories = Category.objects.all()
    context = {'post': post, 'categories': categories}
    tmpl = 'blog/single.html'
    return render(request, tmpl, context)
