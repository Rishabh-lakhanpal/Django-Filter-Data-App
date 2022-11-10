import django_filters
from core.models import Book

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['name', 'author', 'price', 'genre']