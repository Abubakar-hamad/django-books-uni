import os

from django import http
from django.conf import Settings
from django_filters.filters import OrderingFilter
from blog.views import blogs
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, response, Http404
from django.core.paginator import Paginator
from .models import Branch, College, Department, Book
from blog.models import Blog
from .filters import BookFilter
# Create your views here.


def home(request):
    colleges_list = College.objects.all()
    branch_all = Branch.objects.all()
    blogs = list(Blog.objects.all().order_by('-create'))[0:3]
    context = {
        'colleges_list': colleges_list,
        'branch_all': branch_all,
        'blogs': blogs
    }
    return render(request, 'home.html', context)


def colleges_list(request):
    colleges_list = College.objects.all()
    context = {'colleges_list': colleges_list}
    return render(request, 'college/colleges.html', context)


def college_det(request, id):
    college_det = College.objects.get(id=id)
    colleges_list = College.objects.all()
    context = {'college_det': college_det, 'colleges_list': colleges_list}
    return render(request, 'college/college_det.html', context)


def depart(request):
    pass


def branch(request):
    all_branch = Branch.objects.all()
    return render(request, 'branch.html', {"all_branch": all_branch})


def book(request):
    all_book = Book.objects.all()
    filter = BookFilter(request.GET, queryset=all_book)
    all_book = filter.qs
    paginator = Paginator(all_book, 6)  # Show 25 contacts per page.
    page = request.GET.get('page')
    all_book = paginator.get_page(page)

    context = {'all_book': all_book, 'filter': filter, 'page': page}
    return render(request, 'book/book.html', context)


# def download(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type="applications/pdf")
#             response[
#                 'Content-Desposition'] = 'inline,filename=' + os.path.basename(
#                     file_path)
#             return response
#     raise Http404
