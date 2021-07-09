from django.shortcuts import render
from django.views import generic

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import Book, Profile, Author, Publisher
from .serializers import AuthorSerializer, BookSerializer, PublisherSerializer


def index(request):
    """ handling home page """
    num_authors = Author.objects.all().count()
    num_books = Book.objects.all().count()
    num_publishers = Publisher.objects.all().count()

    context = {
        'num_authors': num_authors,
        'num_books': num_books,
        'num_publishers': num_publishers,
    }
    return render(request, 'index.html', context)


# APIs:

class AuthorListCreteAPIView(APIView):
    """ retrieving and creating authors """

    def get(self, request):
        """ retreiving author objects """
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ creating author object """
        serializer = AuthorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class AuthorsBookListAPIView(APIView):
    """ retrieving author books objects """

    def get(self, request, author_id):
        """ retrieving author's books """
        author = Author.objects.get(id=author_id)
        book = Book.objects.filter(author=author)
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)


class PublisherListAPIView(APIView):
    """ retrieving Publishers Listing """

    def get(self, request):
        """ retrieving publisher objects """
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        return Response(serializer.data)


class PublisherBooksListAPIView(APIView):
    """ retrieving publisher"""

    def get(self, request, publisher_id):
        publisher = Publisher.objects.get(id=publisher_id)
        books = Book.objects.filter(publisher=publisher)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookListCreateAPIView(APIView):
    """ retrieving book listing and creating book objects """

    def get(self, request):
        """ retreiving book objects """
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ creating book object """
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)