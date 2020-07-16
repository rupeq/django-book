from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView
)

from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BooksList, BooksCreate

# Create your views here.


# fetch spec obj from db [1]
class BooksView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksList
    # filter
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('title', 'author_name')

# fetch all [2]
class BooksFullView(RetrieveAPIView):
    """Complete list of books"""
    queryset = Book.objects.all()
    serializer_class = BooksCreate

# add new [3]
class BooksCreateView(CreateAPIView):
    """Add new book"""
    serializer_class = BooksCreate
