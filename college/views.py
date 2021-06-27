from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Branch, College, Department, Book
# Create your views here.


def home(request):
    colleges_list = College.objects.all()
    branch_all = Branch.objects.all()
    context = {'colleges_list': colleges_list, 'branch_all': branch_all}
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
    pass


def book_des(request, id):
    pass
