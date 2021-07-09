from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from .views import Author, Book, Publisher
from .serializers import BookSerializer, AuthorSerializer, PublisherSerializer


def sample_author(first_name='testfirstname', last_name='testlastname'):
    """ create sample author object """
    return Author.objects.create(first_name=first_name, last_name=last_name)

def sample_publisher(name='testname', phone='09100000000', address='testaddress'):
    """ create sample publisher object """
    return Publisher.objects.create(name=name, phone=phone, address=address)

def sample_book(author, publisher, title='testtitle', page_number='1000'):
    """ create sample book object """
    return Book.objects.create(author=author, publisher=publisher, title=title, page_number=page_number)


class AuthorApiTests(TestCase):
    """ tests for author api """

    def setUP(self):
        self.client = APIClient()

    def test_retrieve_authors(self):
        """ test retrieving list of authors """
        sample_author()
        sample_author()

        res = self.client.get(reverse('authors'))
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        self.assertEqual(res.data, serializer.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_authors(self):
        """ test create author objects """
        payload = {
            'first_name': 'testname1',
            'last_name': 'testname2',
            'nickname': 'testnick1'
        }

        res = self.client.post(reverse('authors'), payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        author = Author.objects.get(id=res.data['id'])

        for key in payload.keys():
            self.assertEqual(payload[key], getattr(author, key))


class AuthorsBookApiTests(TestCase):
    """ tests for specific authors books """

    def setUp(self):
        self.client = APIClient()
        self.dastayoski = Author.objects.create(
            first_name='something', last_name='something2', nickname='dastayoski'
        )

    def test_retrieve_single_author(self):
        """ test retrieve specific author """
        author_est= sample_author()
        publisher_test = sample_publisher()
        sample_book(author=author_est, publisher=publisher_test)
        res = self.client.get(reverse('author_books'), kwargs={'id': self.dastayoski.id})
        author = Author.objects.get(id=self.dastayoski.id)
        book = Book.objects.get(author=author)
        # serializer = AuthorSerializer(author)
        serializer = BookSerializer(book)
        self.assertEqual(res.data, serializer.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

