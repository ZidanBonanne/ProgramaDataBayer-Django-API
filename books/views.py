
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from books.models import Books
from books.api.serializers import BooksSeriaLizer


class BooksList(generics.ListCreateAPIView):
    queryset= Books.objects.all()
    serializer_class = BooksSeriaLizer


class BooksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Books.objects.all()
    serializer_class = BooksSeriaLizer
