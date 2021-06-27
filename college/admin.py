from django.contrib import admin

# Register your models here.
from .models import College, Department, Book, Branch

admin.site.register(Department)
admin.site.register(College)
admin.site.register(Book)
admin.site.register(Branch)
