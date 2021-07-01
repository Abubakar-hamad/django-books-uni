from typing import Container
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from django.db import models
from datetime import datetime
from django.utils.timezone import timezone


# Create your models here.
class Blog(models.Model):

    titel = models.CharField(max_length=300)
    author = models.CharField(max_length=100, default='admin')
    contents = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='static/img/Blogs', null=True)

    create = models.DateTimeField(auto_now_add=True,
                                  verbose_name=_("Created At"))

    def __str__(self):
        return self.titel

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'id': self.id})
