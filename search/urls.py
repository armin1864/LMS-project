from django.urls import path
from .views import search_books

urlpatterns = [
    # these three are for example commented views
    # path('category/<str:category>/', search_books_by_category, name='search_books_by_category'),
    # path('title/<str:title>/', search_books_by_title, name='search_books_by_title'),
    # path('author/<str:author>/', search_books_by_author, name='search_books_by_author')

    path('', search_books, name='search books')
]
