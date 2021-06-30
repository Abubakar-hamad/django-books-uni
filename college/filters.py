import django_filters
from django.utils.translation import ugettext_lazy as _

from .models import Book


class BookFilter(django_filters.FilterSet):
    # Btitle = django_filters.CharFilter(lookup_expr=_('icontains'))

    class Meta:
        model = Book
        fields = ['Bcollge', 'Bdepart', 'Bclass']
