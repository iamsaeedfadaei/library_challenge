from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.utils import json

from .views import Author, Book, Publisher
from .serializers import BookSerializer, AuthorSerializer, PublisherSerializer

def detail_url(author_id):
    """return recipe detail url"""
    return reverse('author-books', args=[author_id])


def sample_author(first_name='testfirstname', last_name='testlastname'):
    """ create sample author object """
    return Author.objects.create(first_name=first_name, last_name=last_name)

def sample_publisher(name='testname', phone='09100000000', address='testaddress'):
    """ create sample publisher object """
    return Publisher.objects.create(name=name, phone=phone, address=address)

# def sample_book(title='testtitle', page_number='1000'):
#     """ create sample book object """
#     return Book.objects.create(title=title, page_number=page_number)

def sample_book(publisher, **params):
    """create and return a sampel book"""
    defaults = {
        'title': 'Sample Book',
        'page_number': 10,
    }
    defaults.update(params)
    return Book.objects.create(publisher=publisher, **defaults)


class AuthorApiTests(TestCase):
    """ tests for author api """

    def setUP(self):
        self.client = APIClient()

    def test_retrieve_authors(self):
        """ test for retrieving list of authors """
        sample_author()
        sample_author()

        res = self.client.get(reverse('authors'))
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        self.assertEqual(res.data, serializer.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_authors(self):
        """ test for creating author objects """
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


class BookApiTests(TestCase):
    """ tests for book objects """

    def setUp(self):
        self.client = APIClient()
        self.publisher = Publisher.objects.create(
            name='pubtest', phone='09100000000', address='testaddr'
        )

    def test_retrieve_books(self):
        """ test for retrieving book list objects """
        book = sample_book(publisher=self.publisher)
        book.author.add(sample_author())
        # book.publisher.add(sample_publisher())

        res = self.client.get(reverse('books'))
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(res.data, serializer.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_books(self):
        """ test create book objects """
        author = sample_author()
        payload = {
            'title': 'test book',
            'page_number': 10,
            'author': [author.id,],
        }

        res = self.client.post(
            reverse('books'),
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)


class PublisherApiTest(TestCase):
    """ tests for publisher objects """

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_publishers(self):
        """ tests for retrieving publisher list objects """
        sample_publisher()
        sample_publisher()

        res = self.client.get(reverse('publishers'))
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        self.assertEqual(res.data, serializer.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)