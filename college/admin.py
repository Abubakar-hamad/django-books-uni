from django.contrib import admin

# Register your models here.
from . models import College, Department,  Book

admin.site.register(Department)
admin.site.register(College)
admin.site.register(Book)
