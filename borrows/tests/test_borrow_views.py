import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from user_profile.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from authors.models import Authors
from books.models import Books
from borrows.models import BorrowTransactions


def get_jwt_token(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


def create_test_book():
    author = Authors.objects.create(name="Test Author")
    book = Books.objects.create(title="Test Book", author=author, description="Test description",
                                isbn="Test ISBN", category="Test Category")
    return book


@pytest.mark.django_db
def test_borrow_book():
    client = APIClient()
    user = User.objects.create(username='test username', password='test', email='test@test.com')
    token = get_jwt_token(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    book = create_test_book()
    data = {
        'id': book.pk,
        'end_borrow_date': '2025-01-10'
    }

    url = reverse('add_borrow')
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data == 'successful borrow'


@pytest.mark.django_db
def test_borrow_book_borrowed():
    client = APIClient()
    user = User.objects.create(username='test username', password='test', email='test@test.com')
    token = get_jwt_token(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    book = create_test_book()
    book.is_borrowed = True
    book.save()
    data = {
        'id': book.pk,
        'end_borrow_date': '2025-01-10'
    }

    url = reverse('add_borrow')
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['error'] == 'this book already borrowed'


@pytest.mark.django_db
def test_borrow_book_reserved():
    client = APIClient()
    user = User.objects.create(username='test username', password='test', email='test@test.com')
    token = get_jwt_token(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    book = create_test_book()
    book.is_reserved = True
    book.save()
    data = {
        'id': book.pk,
        'end_borrow_date': '2025-01-10'
    }

    url = reverse('add_borrow')
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['error'] == 'this book already reserved by other user'


@pytest.mark.django_db
def test_return_book():
    client = APIClient()
    user = User.objects.create(username='test username', password='test', email='test@test.com')
    token = get_jwt_token(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    book = create_test_book()
    BorrowTransactions.objects.create(borrower=user, book=book)
    data = {
        'id': book.pk,
    }

    url = reverse('return_borrow')
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data == 'successful return'
