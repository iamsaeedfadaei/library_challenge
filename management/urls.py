from django.urls import path
from . import views


urlpatterns = [
    path('author/', views.AuthorListCreteAPIView.as_view(), name='authors'),
    path('author/<int:author_id>/book/', views.AuthorsBookListAPIView.as_view(), name='author_books'),
    path('publisher/', views.PublisherListAPIView.as_view(), name='publishers'),
    path('publisher/<int:publisher_id>/book/', views.PublisherBooksListAPIView.as_view(), name='publisher_books'),
    path('book/', views.BookListCreateAPIView.as_view(), name='books'),
]