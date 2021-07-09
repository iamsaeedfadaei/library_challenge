from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse


# from django.contrib.auth.models import User

class Profile(models.Model):
    """representing users"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='users/%Y/%m/%d/',
                               blank=True)

    def get_absolute_url(self):
        """accessing a particular user by url."""
        return reverse('profile-detail', args=[str(self.id)])

    def __str__(self):
        "representing user object by username"
        return self.user.username


class Book(models.Model):
    """representing the books"""
    title = models.CharField(max_length=240)
    page_number = models.IntegerField()
    publish_Date = models.DateTimeField(default=timezone.now)
    publisher = models.ForeignKey('Publisher', related_name='publisher_books', on_delete=models.CASCADE)
    author = models.ManyToManyField('Author', related_name='book_author')

    def get_absolute_url(self):
        """accessing a particular book by url."""
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        "representing book object by title"
        return self.title


class Author(models.Model):
    """representing book authors"""
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """accessing a particular author by url."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """representing the author object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)


class Publisher(models.Model):
    """representing book publishers"""
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=500)
