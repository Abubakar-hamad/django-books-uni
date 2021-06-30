from typing import ContextManager
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Blog
# Create your views here.


def blogs(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 1)  # Show 25 contacts per page.
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    blog_recent = list(Blog.objects.all().order_by('-create'))[0:3]

    context = {'blogs': blogs, 'blog_recent': blog_recent}
    return render(request, 'blogs.html', context)


def blog_detail(request, id):
    blog_detail = Blog.objects.get(id=id)
    blogs = Blog.objects.all()
    blog_recent = list(Blog.objects.all().order_by('-create'))[0:2]
    context = {
        'blog_detail': blog_detail,
        'blogs': blogs,
        'blog_recent': blog_recent
    }
    return render(request, 'blog_detail.html', context)
