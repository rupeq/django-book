from rest_framework import serializers
from .models import Book


class BooksList(serializers.ModelSerializer):
    """Book list"""
    class Meta:
        model = Book
        fields = ("title", "author_name")

class BooksCreate(serializers.ModelSerializer):
    """Add new book"""
    class Meta:
        model = Book
        fields = '__all__'



