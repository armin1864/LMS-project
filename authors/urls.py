from django.urls import path
from .views import authors_list, author_bio, author_books

urlpatterns = [
    path('', authors_list, name='authors_list'),
    path('<int:pk>/bio', author_bio, name='authors_bio'),
    path('<int:pk>/books', author_books, name='authors_book'),
]
