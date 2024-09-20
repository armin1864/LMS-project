import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from authors.models import Authors
from books.models import Books


@pytest.mark.django_db
def test_get_author_bio():
    client = APIClient()
    author = Authors.objects.create(name="Test Author", bio='Test bio')
    url = reverse('authors_bio', kwargs={'pk': author.pk})
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['bio'] == "Test bio"


@pytest.mark.django_db
def test_get_author_books():
    client = APIClient()
    author = Authors.objects.create(name="Test Author")
    Books.objects.create(title="Test Book", author=author, description="Test description",
                         isbn="Test ISBN", category="Test Category")
    Books.objects.create(title="Test Book2", author=author, description="Test description2",
                         isbn="Test ISBN2", category="Test Category2")
    url = reverse('authors_book', kwargs={'pk': author.pk})
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2


@pytest.mark.django_db
def test_get_author_list():
    client = APIClient()
    url = reverse('authors_list')
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) >= 0
