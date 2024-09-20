import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from user_profile.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from reservations.tests.test_reservation_model import create_test_book
from borrows.models import BorrowTransactions
from reviews.models import ReviewAndRatings


def get_jwt_token(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


@pytest.mark.django_db
def test_review_book():
    client = APIClient()
    user = User.objects.create(username='test username', password='test', email='test@test.com')
    token = get_jwt_token(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    book = create_test_book()
    BorrowTransactions.objects.create(borrower=user, book=book)
    data = {
        'id': book.pk,
        'review': 'test review',
        'rating': 3,
    }

    url = reverse('submit_review')
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data == 'successful review'


@pytest.mark.django_db
def test_review_book_reviewed():
    client = APIClient()
    user = User.objects.create(username='test username', password='test', email='test@test.com')
    token = get_jwt_token(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    book = create_test_book()
    transaction = BorrowTransactions.objects.create(borrower=user, book=book)
    ReviewAndRatings.objects.create(transaction=transaction, book=book,
                                    review="Test Review", rating=2)
    data = {
        'id': book.pk,
        'review': 'test review',
        'rating': 3,
    }

    url = reverse('submit_review')
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['error'] == 'this user already reviewed this book'
