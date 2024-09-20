import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from books.models import Books
from authors.models import Authors


@pytest.mark.django_db
def test_get_books_detail():
    client = APIClient()
    author = Authors.objects.create(name="Test Author")
    book = Books.objects.create(title="Test Book", author=author, description="Test description",
                                isbn="Test ISBN", category="Test Category")

    url = reverse('book_details', kwargs={'pk': book.pk})
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == "Test Book"


@pytest.mark.django_db
def test_get_books():
    client = APIClient()
    url = reverse('books_list', kwargs={'filter': 'available'})
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
