from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

# Create your models here.
Depart_Class = [
    ('اﻷول', 'اﻷول'),
    ('الثاني ', 'الثاني '),
    ('الثالث', 'الثالث'),
    ('الرابع', 'الرابع'),
    ('الخامس', 'الخامس'),
    ('السادس', 'السادس'),
    ('السابع', 'السابع'),
    ('الثامن', 'الثامن'),
    ('التاسع', 'التاسع'),
    ('العاشر', 'العاشر'),
]

SECTION = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
           ('6', '6'), ('7', '7')]

SYSTEM = [('نظام سنوي', ' نظام سنوي'), ('نظام الفصول', 'نظام الفصول')]

STUDY_YEARS = [
    ('2 سنوات', '2 سنوات'),
    ('3 سنوات', '3 سنوات'),
    ('4 سنوات', '4 سنوات'),
    ('5 سنوات', '5 سنوات'),
]


class College(models.Model):
    CLtitle = models.CharField(max_length=200)
    # CLimg = models.ImageField(upload_to = 'static/all/images/colleges', null = True, blank = True)
    CLdescrip = models.TextField(max_length=1000)
    CLdepart = models.CharField(max_length=200,
                                choices=SECTION,
                                verbose_name=_("Department_Number"))

    def get_absolute_url(self):
        return reverse('college:college_detail', kwargs={'id': self.id})

    def __str__(self):
        return self.CLtitle


class Department(models.Model):
    Dcollege = models.ForeignKey('College',
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True,
                                 verbose_name=_("College"))
    Dtitle = models.CharField(max_length=200,
                              verbose_name=_("Department_name"))
    Dsystem = models.CharField(max_length=200,
                               choices=SYSTEM,
                               verbose_name=_("study_system"))

    def __str__(self):
        return self.Dtitle


class Book(models.Model):
    Btitle = models.CharField(max_length=200, verbose_name=_("Book name"))
    pdf = models.FileField(upload_to='static/pdf/Books', null=True, blank=True)
    Bcollge = models.ForeignKey('College',
                                on_delete=models.CASCADE,
                                verbose_name=_("College"))
    Bdepart = models.ForeignKey('Department',
                                on_delete=models.CASCADE,
                                verbose_name=_("Department"))
    Bclass = models.CharField(max_length=20,
                              choices=Depart_Class,
                              verbose_name=_("Semester"))
    Bdescrip = models.TextField(max_length=200, verbose_name=_("Desciption"))

    def __str__(self):
        return self.Btitle


class Branch(models.Model):
    BRtitle = models.CharField(max_length=200)
    BRImg = models.ImageField(upload_to='static/img/branchs')
    BRdescrip = models.TextField(max_length=1000)

    def __str__(self):
        return self.BRtitle


# url(r'^download/(?p<path>.*)$' ,server, {'document_root':settings.MEDIA_ROOT}),