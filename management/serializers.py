from rest_framework import serializers

from .models import Author, Book, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    """serializing author objects"""

    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """ serializing book objects"""
    author = serializers.StringRelatedField(read_only=True)
    # publisher_name = serializers.RelatedField(source='publisher', read_only=True)
    publisher_name = serializers.CharField(source='publisher.name')
    class Meta:
        model = Book
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    """ serializing publisher objects """

    book = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Publisher
        fields = '__all__'

