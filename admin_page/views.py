from books.models import Books
from books.serializers import BooksSerializer
from authors.models import Authors
from authors.serializers import AuthorsSerializer
from user_profile.models import User
from user_profile.serializers import UserSerializer
from borrows.models import BorrowTransactions
from borrows.serializers import BorrowsFullSerializer
from reservations.models import Reservations
from reservations.serializers import ReservationSerializer
from reviews.models import ReviewAndRatings
from reviews.serializers import ReviewSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsAdminUser]


class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    permission_classes = [IsAdminUser]


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class BorrowsViewSet(viewsets.ModelViewSet):
    queryset = BorrowTransactions.objects.all()
    serializer_class = BorrowsFullSerializer
    permission_classes = [IsAdminUser]


class ReservationsViewSet(viewsets.ModelViewSet):
    queryset = Reservations.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAdminUser]


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = ReviewAndRatings.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminUser]
