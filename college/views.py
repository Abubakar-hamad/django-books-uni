from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . models import College, Department, Book
# Create your views here.


def home(request):
    return render(request, 'home.html')


def colleges_list(request):
    colleges_list = College.objects.all()
    context = {
        'colleges_list': colleges_list
    }
    return render(request, 'college/colleges.html', context)


def college_det(request, id):
    college_det = College.objects.get(id=id)
    context = {
        'college_det': college_det
    }
    return render(request, 'college/college_det.html', context)


def depart(request):
    pass


def book(request):
    pass


def book_des(request, id):
    pass
