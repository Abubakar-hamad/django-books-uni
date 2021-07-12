from django.urls import path
from . import views

app_name = 'college'

urlpatterns = [
    path('home', views.home),
    path('college', views.colleges_list),
    path('college/<int:id>', views.college_det, name='college_detail'),
    path('branch', views.branch),
    path('books', views.book),
    path('contact', views.contact),
]
